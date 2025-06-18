# what-time-is-it-now-mcp

現在時刻を取得するシンプルなModel Context Protocol (MCP) サーバー

## 概要

このMCPサーバーは、AIアシスタント（Claude Code、Claude Desktopなど）から現在時刻を取得できるようにする簡単な機能を提供します。日本時間（JST）フォーマットで時刻を返します。

## 必要条件

- Python 3.10以上

## 使い方

### Claude Codeでの使用

#### PyPIからインストールした場合

```bash
# MCPサーバーを追加
claude mcp add what-time-is-it-now-mcp

# またはコマンドラインから直接使用
claude --mcp-server "what-time-is-it-now-mcp:command:what-time-is-it-now-mcp"
```

#### ローカルインストールの場合

```bash
# プロジェクトディレクトリに移動
cd /path/to/what-time-is-it-now-mcp

# MCPサーバーをローカルから追加
claude mcp add . --name what-time-is-it-now-mcp
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
      "cwd": "/path/to/what-time-is-it-now-mcp"
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
what-time-is-it-now-mcp/
├── src/
│   ├── __init__.py
│   └── server.py           # MCPサーバーの実装
├── pyproject.toml          # プロジェクト設定
├── README.md              # このファイル
├── LICENSE                # MITライセンス
└── .mcp.json              # MCP設定ファイル
```

### ローカルでのテスト

```bash
# サーバーを直接起動（stdioモード）
uv run python -m src.server
```

### PyPIへの公開

```bash
# ビルド用ツールをインストール
pip install --upgrade build twine

# パッケージをビルド
python -m build

# PyPIにアップロード（TestPyPIでテスト推奨）
python -m twine upload dist/*
```

## ライセンス

MIT License

## 注意事項

- このプロジェクトではPythonファイルを`src`ディレクトリ直下に配置しています
- MCPサーバー名は`what-time-is-it-now-mcp`として設定されています