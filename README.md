# what-time-is-it-mcp

現在時刻を取得するシンプルなModel Context Protocol (MCP) サーバー

## 概要

このMCPサーバーは、AIアシスタント（Claude Desktopなど）から現在時刻を取得できるようにする簡単な機能を提供します。日本時間（JST）フォーマットで時刻を返します。

## 必要条件

- Python 3.10以上
- uv（Pythonパッケージマネージャー）

## インストール

```bash
# リポジトリをクローン
git clone https://github.com/your-username/what-time-is-it-mcp.git
cd what-time-is-it-mcp

# uvを使って依存関係をインストール
uv sync
```

## 使い方

### Claude Codeでの使用

Claude CodeのCLIから直接MCPサーバーを使用できます：

```bash
# MCPサーバーを有効にしてClaude Codeを起動
claude --mcp-server what-time-is-it-now-mcp:uv:run:python:-m:src.server:/path/to/what-time-is-it-mcp

# または、--mcp-server-dirオプションを使用（.mcp.jsonファイルがある場合）
claude --mcp-server-dir /path/to/what-time-is-it-mcp
```

### Claude Desktopでの設定（オプション）

Claude Desktopでも使用したい場合は、設定ファイル（`~/Library/Application Support/Claude/claude_desktop_config.json`）に以下を追加：

```json
{
  "mcpServers": {
    "what-time-is-it-now-mcp": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "-m",
        "src.server"
      ],
      "cwd": "/path/to/what-time-is-it-mcp"
    }
  }
}
```

### 利用可能なツール

- **get_current_time**: 現在の日本時間（JST）を取得します
  - パラメータ: なし
  - 戻り値: `YYYY-MM-DD HH:MM:SS JST` 形式の時刻文字列

### 使用例

Claude CodeまたはClaude Desktopで以下のように使用できます：

```
「現在の時刻を教えて」と入力すると、get_current_timeツールが呼び出されます
```

## 開発

### プロジェクト構造

```
what-time-is-it-mcp/
├── src/
│   ├── __init__.py
│   └── server.py           # MCPサーバーの実装
├── pyproject.toml          # プロジェクト設定
├── README.md              # このファイル
└── .mcp.json              # MCP設定ファイル
```

### ローカルでのテスト

```bash
# サーバーを直接起動（stdioモード）
uv run python -m src.server
```

## ライセンス

MIT License

## 注意事項

- このプロジェクトではPythonファイルを`src`ディレクトリ直下に配置しています
- MCPサーバー名は`what-time-is-it-now-mcp`として設定されています