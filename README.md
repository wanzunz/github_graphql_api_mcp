[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/wanzunz-github-graphql-api-mcp-badge.png)](https://mseep.ai/app/wanzunz-github-graphql-api-mcp)

# GitHub GraphQL API MCP

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [Español](README_es.md) | [Français](README_fr.md)

A tool based on MCP (Model Context Protocol) for querying and using the GitHub GraphQL API. This project provides a server that allows you to explore the GitHub GraphQL schema and execute GraphQL queries through MCP client tools (such as Claude AI).

## Why Use GitHub GraphQL API

GitHub GraphQL API offers significant advantages over traditional REST APIs:

- **Precise Data Retrieval**: GraphQL allows clients to specify exactly which fields they need, avoiding excess data
- **Reduced Token Consumption**: By requesting only necessary fields, API response size is significantly reduced, lowering AI model token consumption
- **Single Request for Related Data**: One query can retrieve multiple related resources, reducing the number of requests
- **Self-Documenting**: Through its built-in documentation system, you can directly query and understand the API schema without external documentation
- **Strong Type System**: Provides type checking, reducing errors

This project leverages these advantages to provide tools that help you effectively explore the GitHub GraphQL API schema and execute optimized queries, providing AI assistants with efficient GitHub data retrieval capabilities.

## Application Scenarios

### Basic Functions

This tool easily implements the following common operations:

1. **Repository Basic Information Query**: Get repository name, description, star count, branch list, and other basic information
2. **Issue Data Retrieval**: Query issue lists, details, or comment content for specific repositories
3. **User Profile Access**: Retrieve users' personal profiles, contribution statistics, and other public information
4. **Pull Request Status View**: Get PR basic status, comment content, and merge information
5. **Project Dependency Query**: Retrieve project dependency package lists and version information

### Exploratory Advanced Functions

With GraphQL's flexible query capabilities, you can also try to implement the following advanced analysis functions:

1. **Repository Contribution Trend Analysis**: Analyze code update frequency and contributor participation by aggregating commit data, evaluating project activity
2. **Issue Management and Classification**: Organize issue data according to custom conditions, discover problems that need priority handling, and improve project management efficiency
3. **Code Review Pattern Analysis**: Analyze PR comments and review processes, identify common problem patterns, and optimize code review workflow
4. **Contributor Network Visualization**: Build collaboration relationships between project contributors, discover key contributors and areas of expertise
5. **Dependency Health Assessment**: Evaluate the update frequency and potential security issues of project dependencies, providing dependency management suggestions

## Features

- Query GitHub GraphQL schema root types (Query/Mutation)
- Get detailed documentation for specific types
- Query documentation and parameters for specific fields
- Execute GitHub GraphQL API queries directly, precisely retrieving needed data, reducing token consumption
- Multilingual support (English/Chinese/Japanese/Spanish/French)

## Comparison with Official GitHub MCP Server

Compared to the official [github-mcp-server](https://github.com/github/github-mcp-server), this project offers distinct advantages in specific scenarios:

| Feature | GitHub GraphQL API MCP | Official GitHub MCP Server |
|---------|------------------------|----------------------------|
| **Core Mechanism** | Single GraphQL Query | Multiple REST API / Granular Tools |
| **Data Retrieval** | **One-shot**: Fetch repository details, issues, PRs, history, and releases in a single request | **Multi-step**: Requires chaining `search_repositories`, `get_file_contents`, `list_commits`, etc. |
| **Efficiency** | High. Minimizes network latency and round-trips. | Lower for complex data gathering. High latency due to sequential tool calls. |
| **Token Usage** | **Optimized**. Returns only requested fields. | **Higher**. Intermediate tool outputs (full JSON responses) consume context window. |
| **Flexibility** | **High**. Client defines exact data structure needed. | **Fixed**. Client must work with predefined API response structures. |
| **API Coverage** | **Complete**. Access any field exposed by GitHub's GraphQL API. | **Partial**. Limited to the specific REST endpoints hardcoded by the maintainers. |
| **Introspection** | **Built-in**. AI can query the schema to learn about new API fields dynamically. | **None**. AI relies on its training data; cannot discover new API features without tool updates. |
| **Maintainability** | **Zero-code updates**. Often just requires a schema file update to support new GitHub features. | **Code-heavy**. Requires writing new Go handlers and struct definitions for every new feature. |
| **Complexity** | Requires LLM to write GraphQL (supported by schema introspection tools). | Easier for LLMs that prefer simple function calls, but harder to manage state across calls. |

**Example**: To get "latest important updates for a project", this tool can fetch releases, recent commits, and open issues in **one go**, whereas the official server might require 5+ separate tool calls and round trips.

### Why This Matters for AI Agents

1.  **Context Window Efficiency**: Official tools often return massive JSON objects (e.g., a full repository object might be 5KB+). With GraphQL, you fetch only the `name` and `description`, saving 99% of tokens.
2.  **Complex Reasoning**: AI agents often need to traverse relationships (e.g., "Find the author of the PR that closed this Issue"). In REST/Official tools, this is a multi-step "Search -> Get ID -> Get PR -> Get Author" process. In GraphQL, it's a single nested query, allowing the AI to focus on reasoning rather than data plumbing.
3.  **Future Proofing**: When GitHub adds a new feature (e.g., a new field on Discussions), this MCP server can support it immediately via schema introspection, while the official server waits for a code update.

## Prerequisites

- Python 3.10 or higher
- GitHub personal access token (for accessing the GitHub API)
- Poetry (recommended dependency management tool)

## Installation & Usage

We recommend using [uv](https://github.com/astral-sh/uv) for management, which is currently the fastest and simplest Python project management tool. Alternatively, you can use standard pip.

### Method 1: Using uv (Recommended, Fastest)

With uv, you don't need to manually create virtual environments or install dependencies; it handles everything for you automatically.

1.  **Install uv** (Skip if already installed):
    ```bash
    # MacOS / Linux
    curl -lsSf https://astral.sh/uv/install.sh | sh

    # Windows
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

2.  **Configure Environment Variables**:
    Copy `.env.example` to `.env` and fill in your GitHub Token:
    ```bash
    cp .env.example .env
    # Edit .env file and fill in your token
    ```

3.  **One-click Run**:
    ```bash
    uv run github_graphql_api_mcp_server.py
    ```
    *uv will automatically create a virtual environment, download and install all dependencies, and then start the server.*

### Method 2: Standard pip

If you prefer not to install extra tools, you can use the traditional Python method:

1.  **Create and Activate Virtual Environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**:
    Create and configure `.env` file as above.

4.  **Run**:
    ```bash
    python github_graphql_api_mcp_server.py
    ```

## Configure in Claude Desktop

You can configure this MCP server in the Claude desktop app for one-click startup:

1. Open the Claude desktop app
2. Go to settings, find the MCP server configuration section
3. Add the following configuration (modify according to your actual path):

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/path/to/uv",
            "args": [
                "run",
                "--directory",
                "<project path>",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

Configuration example (using uv):

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/Users/username/.cargo/bin/uv",
            "args": [
                "run",
                "--directory",
                "/Users/username/github/github_graphql_api_mcp/",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

If using standard Python (Method 2):

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/path/to/project/.venv/bin/python",
            "args": [
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

After configuration, you can start the MCP server directly from the Claude desktop app without having to start it manually.

### Available Tools

The server provides the following tools:

1. **print_type_field**: Query fields of GitHub GraphQL schema root types
2. **graphql_schema_root_type**: Get documentation for root types (Query/Mutation)
3. **graphql_schema_type**: Query documentation for specific types
4. **call_github_graphql**: Execute GitHub GraphQL API queries

### Usage Examples

After connecting to the server with an MCP client, you can:

1. Query root type documentation:
   ```
   Use the graphql_schema_root_type tool, parameter type_name="QUERY"
   ```

2. Query fields of specific types:
   ```
   Use the print_type_field tool, parameters type_name="QUERY", type_fields_name="repository"
   ```

3. Query documentation for specific types:
   ```
   Use the graphql_schema_type tool, parameter type_name="Repository"
   ```

4. Execute GraphQL queries:
   ```
   Use the call_github_graphql tool, parameter:
   graphql="""
   query {
     viewer {
       login
       name
     }
   }
   """
   ```

#### Example Screenshot

Below is an example of using the GitHub GraphQL API MCP with Claude:

![GitHub GraphQL API MCP Usage Example](img/github_graphql_usage_example.png)

## Notes

- Make sure your GitHub token has appropriate permissions before use
- The token is stored in the `.env` file, which should not be committed to version control systems
- Queries should comply with GitHub API usage limits

## License

This project is licensed under the MIT License - a very permissive license that allows users to freely use, modify, distribute, and commercialize this software, as long as they retain the copyright notice and license statement.

See [MIT License](https://opensource.org/licenses/MIT) for detailed terms.
