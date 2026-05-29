# Kernel Code Index — Linux 内核代码索引系统

## 项目目标

构建一套针对 Linux 内核代码库的符号索引和语义检索系统，让 AI 能够理解代码结构并回答代码级问题。

## 核心问题

Linux 内核代码量巨大（数千万行），无法直接塞入 LLM 上下文窗口。需要一个中间层，将代码结构提取、索引化，供 AI 检索使用。

## 要解决的问题

- "这个函数被谁调用？" → 调用链索引
- "这个结构体在哪定义？成员有哪些？" → 符号索引
- "这个驱动和哪些 Kconfig 选项相关？" → 依赖索引
- "设备树这个节点对应哪个驱动？" → dts-driver 映射

## 技术方向

1. **符号提取**：用 clangd / ctags / cscope 从内核源码提取函数、结构体、宏、枚举等符号信息
2. **调用链分析**：构建函数调用图（call graph），支持正向/反向查询
3. **依赖分析**：Kconfig → Makefile → 源文件 → 设备树的依赖链
4. **向量化存储**：将符号摘要向量化，存入向量数据库（可复用 qmd 方案）
5. **与现有 Wiki 打通**：代码索引和 E:\Wiki\embedded\wiki 的知识库联合检索

## 竞品调研（2026-05）

**结论：积木都有，没人拼成内核专用方案。**

可复用的现有工具：
- **Aider repo-map** (28k star) — tree-sitter + ctags 提取调用图，有 token 预算裁剪算法，可直接复用
  - https://github.com/Aider-AI/aider
- **Sourcegraph/Cody** — 内核已在公共实例上索引，但自部署要企业版
- **codebase-intelligence** (49 star) — AST + call graph + embeddings CLI 工具
  - https://github.com/Thibault-Knobloch/codebase-intelligence
- **codebase-RAG** (15 star) — MCP server，增量索引，多语言解析
  - https://github.com/bluewings1211/codebase-RAG

空白地带（我们的切入点）：
- 没人做过 Kconfig/Makefile 依赖图解析供 AI 消费
- 没有内核专用的调用图（syscall path、driver probe chain）
- 没人用 clangd compile_commands.json 做内核 RAG
- 没有子系统边界识别（mm/、fs/、net/、drivers/）

## 关键文件/工具

- Linux 内核源码（需要指定版本）
- clangd / universal-ctags / cscope
- Aider repo-map（可复用的调用图提取逻辑）
- 向量数据库（qmd 或其他方案）
- Python 脚本做提取和索引管道

## 阶段规划

### Phase 1：符号提取 MVP
- 选定一个内核版本和子系统（比如 drivers/gpio）
- 用 ctags/clangd 提取符号信息
- 存入可查询的结构（JSON/SQLite）

### Phase 2：调用链构建
- 解析函数调用关系
- 支持"谁调用了 X"和"X 调用了谁"的查询

### Phase 3：向量化 + AI 集成
- 符号摘要向量化
- 接入 AI，支持自然语言查询代码结构

### Phase 4：与 Wiki 联合检索
- 代码索引 + 知识库统一搜索入口
- AI 回答时同时引用代码位置和文档说明

## 验证方式

- 能查询指定子系统的函数列表和调用关系
- AI 能回答"GPIO 子系统的 probe 流程"这类问题并给出代码位置
- 查询延迟在秒级以内
