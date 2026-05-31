# 使用指南：搭建你自己的内核代码检索工具

本指南帮助你基于 kernel-code-index 项目，搭建针对任意 Linux 内核子系统的代码检索工具。

## 1. 环境准备

### 必需

| 依赖 | 版本 | 用途 |
|------|------|------|
| Python | 3.10+ | 索引管道和 MCP server |
| Node.js | 18+ | 安装 qmd |
| Git | 2.30+ | 获取内核源码（sparse checkout） |

### 可选

| 依赖 | 用途 |
|------|------|
| Claude Code | 通过 MCP 使用索引工具 |
| qmd | 语义搜索（BM25 + 向量检索） |

## 2. 获取项目

```bash
git clone https://github.com/YOUR_USERNAME/kernel-code-index.git
cd kernel-code-index
pip install mcp
```

## 3. 获取内核源码

使用 sparse checkout 只下载你需要的子系统，避免下载整个内核（>2GB）：

```bash
# 示例：索引 GPIO 子系统
git clone --depth 1 --filter=blob:none --sparse https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git kernel-src
cd kernel-src
git sparse-checkout set drivers/gpio include/linux/gpio
cd ..
```

### 常用子系统的 sparse-checkout 路径

| 子系统 | sparse-checkout 路径 |
|--------|---------------------|
| GPIO | `drivers/gpio include/linux/gpio` |
| SPI | `drivers/spi include/linux/spi` |
| I2C | `drivers/i2c include/linux/i2c*` |
| MMC | `drivers/mmc include/linux/mmc` |
| 网络 | `drivers/net include/linux/netdevice.h include/net` |
| 文件系统 | `fs/ext4 include/linux/ext4*` |
| 内存管理 | `mm include/linux/mm.h include/linux/slab.h` |

## 4. 修改索引配置

编辑 `indexer.py`，修改子系统路径：

```python
# 找到这一行，改为你要索引的子系统
SUBSYSTEM = "drivers/gpio"  # 改为你的子系统
```

## 5. 运行索引

```bash
python indexer.py
```

索引完成后会生成 `kernel_index.db` 数据库，包含所有符号和调用关系。

### 验证索引

```bash
python query.py stats          # 查看统计信息
python query.py find gpio_chip # 搜索符号
python query.py functions drivers/gpio/gpiolib.c  # 列出文件函数
```

## 6. 配置 Claude Code MCP

编辑 `.mcp.json`，将 `cwd` 改为你的项目绝对路径：

```json
{
  "mcpServers": {
    "kernel-index": {
      "command": "python",
      "args": ["mcp_server.py"],
      "cwd": "/home/youruser/projects/kernel-code-index"
    }
  }
}
```

Windows 用户：

```json
{
  "mcpServers": {
    "kernel-index": {
      "command": "python",
      "args": ["mcp_server.py"],
      "cwd": "C:/Users/YourName/projects/kernel-code-index"
    }
  }
}
```

配置完成后，在 Claude Code 中即可使用 `find_symbol`、`call_graph` 等工具。

## 7. 配置语义搜索（可选）

语义搜索基于 qmd 引擎，支持自然语言查询代码。

### 7.1 安装 qmd

```bash
npm install -g @tobilu/qmd
```

### 7.2 导出符号文档

```bash
python export_symbols.py
```

这会在 `symbol-docs/` 目录生成每个源文件的 markdown 文档。

### 7.3 创建 qmd collection

```bash
qmd add kernel-symbols symbol-docs/
```

### 7.4 测试搜索

```bash
qmd query "gpio interrupt handling" -c kernel-symbols
```

### 7.5 与 MCP 集成

`mcp_server.py` 中的 `search` 工具会自动调用 qmd。确保 qmd 已安装且 `kernel-symbols` collection 已创建。

如果还需要与 Wiki 文档联合搜索：

```bash
qmd add wiki /path/to/your/wiki/
```

然后修改 `mcp_server.py` 中的 search 函数，将 `-c wiki` 改为你的 Wiki 路径对应的 collection 名称。

## 8. 添加更多子系统

索引完成后，可以通过 MCP 工具动态添加新子系统：

1. 更新 sparse-checkout：
   ```bash
   cd kernel-src
   git sparse-checkout add drivers/spi include/linux/spi
   cd ..
   ```

2. 在 Claude Code 中使用 MCP 工具：
   ```
   reindex_subsystem("drivers/spi")
   ```

或通过 Python 脚本：

```python
from indexer import index_subsystem
index_subsystem("drivers/spi")
```

## 9. 常见问题

### Q: ctags 找不到？

项目自带了 Windows 版 ctags（`tools/ctags_bin/`）。Linux/macOS 用户需要自行安装：

```bash
# Ubuntu/Debian
sudo apt install universal-ctags

# macOS
brew install universal-ctags
```

然后修改 `indexer.py` 中的 `CTAGS_BIN` 路径。

### Q: qmd 安装失败？

确保 Node.js 版本 >= 18：

```bash
node --version
npm install -g @tobilu/qmd
```

Windows 用户需要确保 Git Bash 的 `sh.exe` 在 PATH 中。

### Q: 索引很慢？

ctags 索引速度取决于子系统大小。GPIO 子系统（212 文件）约需 10 秒。更大的子系统（如 `drivers/net`）可能需要几分钟。

### Q: 如何索引整个内核？

不建议。整个内核有数百万行代码，索引数据库会非常大且查询缓慢。建议按子系统分别索引。

### Q: 如何更新索引？

重新运行 `python indexer.py` 会重建数据库。或使用 `reindex_subsystem` MCP 工具增量添加。
