# GitHub GraphQL API MCP

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [Español](README_es.md) | [Français](README_fr.md)

GitHub GraphQL APIのクエリと使用のためのMCP（Model Control Protocol）ベースのツールです。このプロジェクトは、MCP クライアントツール（Claude AIなど）を通じてGitHub GraphQLスキーマを探索し、GraphQLクエリを実行できるサーバーを提供します。

## なぜGitHub GraphQL APIを使用するのか

GitHub GraphQL APIは従来のREST APIに比べて大きな利点があります：

- **必要なデータの正確な取得**：GraphQLはクライアントが必要なフィールドを正確に指定できるため、余分なデータの取得を避けられます
- **トークン消費の削減**：必要なフィールドのみをリクエストすることで、APIレスポンスのサイズが大幅に削減され、AIモデルのトークン消費を抑えられます
- **関連データを一度のリクエストで取得**：一つのクエリで複数の関連リソースを取得でき、リクエスト数を減らせます
- **自己文書化**：内蔵のドキュメントシステムにより、外部ドキュメントなしでAPIスキーマを直接照会し理解できます
- **強力な型システム**：型チェックを提供し、エラーを減らします

このプロジェクトはこれらの利点を活用し、GitHub GraphQL APIスキーマを効果的に探索し、最適化されたクエリを実行するためのツールを提供して、AIアシスタントに効率的なGitHubデータ取得機能を提供します。

## アプリケーションシナリオ

### 基本機能

このツールは以下の一般的な操作を簡単に実行できます：

1. **リポジトリ基本情報クエリ**：リポジトリ名、説明、スター数、ブランチリストなどの基本情報を取得
2. **課題データの検索**：特定のリポジトリの課題リスト、詳細、またはコメント内容をクエリ
3. **ユーザープロフィールアクセス**：ユーザーの個人プロフィール、貢献統計などの公開情報を取得
4. **Pull Requestステータス表示**：PRの基本ステータス、コメント内容、マージ情報を取得
5. **プロジェクト依存関係クエリ**：プロジェクトの依存パッケージリストとバージョン情報を検索

### 高度な探索機能

GraphQLの柔軟なクエリ機能により、以下の高度な分析機能も実装できます：

1. **リポジトリ貢献傾向分析**：コミットデータを集計して、コード更新頻度と貢献者の参加度を分析し、プロジェクトの活動度を評価
2. **課題管理と分類**：カスタム条件に従って課題データを整理し、優先的に処理すべき問題を発見してプロジェクト管理効率を向上
3. **コードレビューパターン分析**：PRコメントとレビュープロセスを分析し、共通の問題パターンを特定してコードレビューワークフローを最適化
4. **貢献者ネットワーク可視化**：プロジェクト貢献者間のコラボレーション関係を構築し、主要な貢献者と専門分野を発見
5. **依存関係の健全性評価**：プロジェクト依存関係の更新頻度と潜在的なセキュリティ問題を評価し、依存関係管理の提案を提供

## 特徴

- GitHub GraphQLスキーマのルートタイプ（Query/Mutation）のクエリ
- 特定タイプの詳細ドキュメントの取得
- 特定フィールドのドキュメントとパラメータのクエリ
- GitHub GraphQL APIクエリを直接実行し、必要なデータを正確に取得してトークン消費を削減
- 多言語サポート（英語/中国語/日本語など）

## 前提条件

- Python 3.10以上
- GitHub個人アクセストークン（GitHub APIにアクセスするため）
- Poetry（推奨される依存関係管理ツール）

## インストール

1. リポジトリをクローン：

```bash
git clone https://github.com/wanzunz/github_graphql_api_mcp.git
cd github_graphql_api_mcp
```

2. Poetryを使用して依存関係をインストール：

```bash
# まだPoetryをインストールしていない場合は、最初にインストール：
# curl -sSL https://install.python-poetry.org | python3 -

# Poetryを使用して依存関係をインストール
poetry install

# 仮想環境を有効化
poetry shell
```

Poetryを使用しない場合は、従来の方法を使用できます：

```bash
# 仮想環境を作成して有効化
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
# または
.venv\Scripts\activate  # Windows

# 依存関係をインストール
pip install -e .
```

3. 環境変数を設定：

`.env`ファイルを作成し、GitHubの個人アクセストークンを追加：

```
GITHUB_TOKEN="your_github_token_here"
```

`.env.example`ファイルをコピーして作成できます：

```bash
cp .env.example .env
```

その後、`.env`ファイルを編集し、`your_github_token_here`を実際のGitHubトークンに置き換えます。

## 使用方法

### サーバーの起動

Poetry仮想環境が有効化されていることを確認し（`poetry shell`）、次に実行：

#### 実行

```bash
python github_graphql_api_mcp_server.py
```

サーバーが起動したら、MCPクライアント（Claude AIなど）を通じて接続できます。

### Claudeデスクトップでの設定

Claudeデスクトップアプリでこのサーバーを設定し、ワンクリックで起動できます：

1. Claudeデスクトップアプリを開く
2. 設定に移動し、MCPサーバー設定セクションを見つける
3. 以下の設定を追加（実際のパスに合わせて修正）：

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "<Pythonインタープリターのパス>",
            "args": [
                "--directory",
                "<プロジェクトパス>",
                "run",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

設定例：

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

condaやその他の環境管理ツールを使用している場合：

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

設定完了後、Claudeデスクトップアプリから直接MCPサーバーを起動できるため、手動での起動が不要になります。

### 利用可能なツール

サーバーは以下のツールを提供します：

1. **print_type_field**：GitHub GraphQLスキーマのルートタイプのフィールドをクエリ
2. **graphql_schema_root_type**：ルートタイプ（Query/Mutation）のドキュメントを取得
3. **graphql_schema_type**：特定タイプのドキュメントをクエリ
4. **call_github_graphql**：GitHub GraphQL APIクエリを実行

### 使用例

MCPクライアントでサーバーに接続した後、以下が可能です：

1. ルートタイプのドキュメントをクエリ：
   ```
   graphql_schema_root_typeツールを使用、パラメータtype_name="QUERY"
   ```

2. 特定タイプのフィールドをクエリ：
   ```
   print_type_fieldツールを使用、パラメータtype_name="QUERY", type_fields_name="repository"
   ```

3. 特定タイプのドキュメントをクエリ：
   ```
   graphql_schema_typeツールを使用、パラメータtype_name="Repository"
   ```

4. GraphQLクエリを実行：
   ```
   call_github_graphqlツールを使用、パラメータ：
   graphql="""
   query {
     viewer {
       login
       name
     }
   }
   """
   ```

#### スクリーンショット例

以下はGitHub GraphQL API MCPをClaudeで使用する例です：

![GitHub GraphQL API MCP 使用例](img/github_graphql_usage_example.png)

## 注意事項

- 使用前にGitHubトークンが適切な権限を持っていることを確認
- トークンは`.env`ファイルに保存され、このファイルはバージョン管理システムにコミットすべきではない
- クエリはGitHub APIの使用制限に従う必要がある

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。これは非常に寛容なライセンスで、著作権表示とライセンス表示を保持する限り、ユーザーは自由にこのソフトウェアを使用、修正、配布、商用化することができます。

詳細な条件については[MITライセンス](https://opensource.org/licenses/MIT)を参照してください。 