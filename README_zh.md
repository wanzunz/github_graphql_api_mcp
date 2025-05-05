# GitHub GraphQL API MCP

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [Español](README_es.md) | [Français](README_fr.md)

这是一个基于 MCP (Model Control Protocol) 的工具，用于查询和使用 GitHub GraphQL API。项目提供了一个服务器，允许你通过 MCP 客户端工具（如 Claude AI）探索 GitHub GraphQL 架构并执行 GraphQL 查询。

## 为什么使用 GitHub GraphQL API

GitHub GraphQL API 相比传统 REST API 具有显著优势：

- **精确获取所需数据**：GraphQL 允许客户端精确指定需要的字段，避免获取多余数据
- **减少 Token 消耗**：通过只请求必要字段，可以显著减少 API 响应大小，从而降低 AI 模型的 Token 消耗
- **单次请求获取关联数据**：一次查询可以获取多个相关资源，减少请求次数
- **自我文档化**：通过内置的文档系统，可以直接查询和了解 API 架构，无需外部文档
- **强类型系统**：提供类型检查，减少错误

本项目充分利用这些优势，提供工具帮助你有效地探索 GitHub GraphQL API 架构并执行优化的查询，为 AI 助手提供高效的 GitHub 数据获取能力。

## 应用场景

### 基础功能

本工具可以轻松实现以下常见操作：

1. **仓库基本信息查询**：获取仓库名称、描述、星标数、分支列表等基本信息
2. **议题数据检索**：查询特定仓库的议题列表、详情或评论内容
3. **用户资料获取**：检索用户的个人资料、贡献统计等公开信息
4. **Pull Request 状态查看**：获取 PR 的基本状态、评论内容和合并信息
5. **项目依赖查询**：检索项目的依赖包清单及版本信息

### 探索性高级功能

借助 GraphQL 的灵活查询能力，你还可以尝试实现以下高级分析功能：

1. **仓库贡献趋势分析**：通过聚合提交数据，分析代码更新频率和贡献者参与度，评估项目活跃度
2. **议题管理与分类**：根据自定义条件组织议题数据，发现需要优先处理的问题，提升项目管理效率
3. **代码审查模式分析**：分析 PR 评论和审查过程，识别常见问题模式，优化代码审查流程
4. **贡献者网络可视化**：构建项目贡献者之间的协作关系，发现关键贡献者和专长领域
5. **依赖健康状况评估**：评估项目依赖的更新频率和潜在安全问题，提供依赖管理建议

## 特性

- 查询 GitHub GraphQL 架构的根类型（Query/Mutation）
- 获取特定类型的详细文档
- 查询特定字段的文档和参数
- 直接执行 GitHub GraphQL API 查询，精确获取所需数据，减少 Token 消耗
- 中英双语支持

## 前提条件

- Python 3.10 或更高版本
- GitHub 个人访问令牌（用于访问 GitHub API）
- Poetry（推荐的依赖管理工具）

## 安装

1. 克隆项目仓库：

```bash
git clone https://github.com/wanzunz/github_graphql_api_mcp.git
cd github_graphql_api_mcp
```

2. 使用 Poetry 安装依赖：

```bash
# 如果你还没有安装 Poetry，请先安装：
# curl -sSL https://install.python-poetry.org | python3 -

# 使用 Poetry 安装依赖
poetry install

# 激活虚拟环境
poetry shell
```

如果你不使用 Poetry，也可以使用传统方式：

```bash
# 创建并激活虚拟环境
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
# 或
.venv\Scripts\activate  # Windows

# 安装依赖
pip install -e .
```

3. 配置环境变量：

创建 `.env` 文件并添加你的 GitHub 个人访问令牌：

```
GITHUB_TOKEN="your_github_token_here"
```

你可以通过复制 `.env.example` 文件来创建：

```bash
cp .env.example .env
```

然后编辑 `.env` 文件，将 `your_github_token_here` 替换为你的实际 GitHub 令牌。

## 使用方法

### 启动服务器

确保你已激活 Poetry 虚拟环境（`poetry shell`），然后：

#### 运行

```bash
python github_graphql_api_mcp_server.py
```

服务器启动后，你可以通过 MCP 客户端（如 Claude AI）连接到它。

### 在 Claude 桌面端配置

你可以在 Claude 桌面端中配置此 MCP 服务器，实现一键启动：

1. 打开 Claude 桌面端
2. 进入设置，找到 MCP 服务器配置部分
3. 添加以下配置（根据你的实际路径修改）：

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "<你的Python解释器路径>",
            "args": [
                "--directory",
                "<项目路径>",
                "run",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

配置示例：

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/usr/bin/python3",
            "args": [
                "--directory",
                "/home/user/projects/github_graphql_api_mcp/",
                "run",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

如果你使用 conda 或其他环境管理工具：

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/opt/miniconda3/bin/python",
            "args": [
                "--directory",
                "/Users/username/github/github_graphql_api_mcp/",
                "run",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

配置完成后，你可以直接从 Claude 桌面端启动 MCP 服务器，无需手动启动。

### 可用工具

服务器提供以下工具：

1. **print_type_field**：查询 GitHub GraphQL 架构根类型的字段
2. **graphql_schema_root_type**：获取根类型（Query/Mutation）的文档
3. **graphql_schema_type**：查询特定类型的文档
4. **call_github_graphql**：执行 GitHub GraphQL API 查询

### 使用示例

使用 MCP 客户端连接到服务器后，你可以：

1. 查询根类型文档：
   ```
   使用 graphql_schema_root_type 工具，参数 type_name="QUERY"
   ```

2. 查询特定类型的字段：
   ```
   使用 print_type_field 工具，参数 type_name="QUERY", type_fields_name="repository"
   ```

3. 查询特定类型的文档：
   ```
   使用 graphql_schema_type 工具，参数 type_name="Repository"
   ```

4. 执行 GraphQL 查询：
   ```
   使用 call_github_graphql 工具，参数：
   graphql="""
   query {
     viewer {
       login
       name
     }
   }
   """
   ```

## 注意事项

- 使用前请确保你的 GitHub 令牌具有适当的权限
- 令牌存储在 `.env` 文件中，该文件不应该被提交到版本控制系统中
- 查询时应遵循 GitHub API 的使用限制

## 许可证

本项目采用 MIT 许可证 - 这是一个非常宽松的许可证，允许用户自由地使用、修改、分发和商业化本软件，只需保留版权声明和许可证声明即可。

详细条款请参见 [MIT 许可证](https://opensource.org/licenses/MIT)。 