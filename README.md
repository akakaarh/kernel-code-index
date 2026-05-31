# Kernel Code Index

Linux 内核代码符号索引系统，为 AI 提供内核代码结构理解能力。通过 MCP (Model Context Protocol) 与 Claude Code 集成，支持符号查询、调用链分析和语义搜索。

## 功能

- **符号查询** — 按名称搜索函数、结构体、宏、枚举等符号
- **文件符号列表** — 查看指定源文件中定义的所有符号
- **调用图** — 查看函数的调用者/被调用者，支持多层展开
- **调用链** — BFS 查找两个函数之间的调用路径
- **语义搜索** — 基于 qmd 向量引擎的自然语言代码搜索
- **子系统索引** — 动态添加新的内核子系统到索引

## 快速开始

### 环境要求

- Python 3.10+
- Node.js（用于安装 qmd）
- [universal-ctags](https://ctags.io/)（项目自带 Windows 版本在 `tools/`）

### 安装

```bash
git clone https://github.com/YOUR_USERNAME/kernel-code-index.git
cd kernel-code-index

# 安装 Python 依赖
pip install mcp

# 安装 qmd（语义搜索需要）
npm install -g @tobilu/qmd
```

### 索引内核子系统

```bash
# 1. 获取内核源码（sparse checkout）
git clone --depth 1 --filter=blob:none --sparse https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git kernel-src
cd kernel-src
git sparse-checkout set drivers/gpio include/linux/gpio
cd ..

# 2. 运行索引
python indexer.py
```

### 配置 Claude Code MCP

编辑 `.mcp.json`，将路径改为你的项目路径：

```json
{
  "mcpServers": {
    "kernel-index": {
      "command": "python",
      "args": ["mcp_server.py"],
      "cwd": "/your/path/to/kernel-code-index"
    }
  }
}
```

### 配置 qmd 语义搜索

```bash
# 导出符号文档
python export_symbols.py

# 创建 qmd collection
qmd add kernel-symbols symbol-docs/
```

详细步骤见 [docs/setup-guide.md](docs/setup-guide.md)。

## MCP 工具列表

| 工具 | 说明 |
|------|------|
| `find_symbol` | 按名称搜索符号（支持子串匹配） |
| `list_functions` | 列出文件中的所有函数 |
| `search_by_kind` | 按类型列出符号（function/struct/macro/enum...） |
| `file_symbols` | 查看文件的完整符号概览 |
| `index_stats` | 索引统计信息 |
| `reindex_subsystem` | 索引新的内核子系统 |
| `call_graph` | 函数调用图（支持多层展开） |
| `call_chain` | 两函数间的调用路径（BFS） |
| `search` | 语义搜索（BM25 + 向量混合检索） |

## 项目结构

```
kernel-code-index/
├── mcp_server.py         # MCP server 主程序（9 个工具）
├── indexer.py            # ctags 符号提取管道
├── call_graph.py         # 调用图构建和查询
├── export_symbols.py     # 符号导出为 markdown
├── query.py              # CLI 查询工具
├── schema.sql            # SQLite 数据库 schema
├── .mcp.json             # MCP server 注册配置
├── tools/                # ctags 二进制工具
├── symbol-docs/          # 导出的符号文档（qmd 用）
└── kernel-src/           # 内核源码（需自行获取）
```

## 技术栈

- **ctags** — C 语言符号提取
- **SQLite** — 符号和调用关系存储
- **MCP (FastMCP)** — AI 工具协议
- **qmd** — BM25 + 向量混合检索引擎
