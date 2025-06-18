# what-time-is-it-now-mcp

現在時刻を取得するシンプルなModel Context Protocol (MCP) サーバー

## 概要

このMCPサーバーは、AIアシスタント（Claude Code、Claude Desktopなど）から現在時刻を取得できるようにする簡単な機能を提供します。日本時間（JST）フォーマットで時刻を返します。

## 使い方

### Claude Codeでの使用

```bash
# MCPサーバーを追加
claude mcp add what-time-is-it-now-mcp
```

### Claude Desktopでの使用

Claude Desktopの場合は、設定ファイル（`~/Library/Application Support/Claude/claude_desktop_config.json`）に以下を追加：

```json
{
  "mcpServers": {
    "what-time-is-it-now-mcp": {
      "command": "what-time-is-it-now-mcp"
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

## ライセンス

MIT License

