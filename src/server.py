"""what-time-is-it-mcp Server - 現在時刻を提供するMCPサーバー"""

from datetime import datetime
from zoneinfo import ZoneInfo
from fastmcp import FastMCP

# MCPサーバーのインスタンスを作成
mcp = FastMCP("what-time-is-it-now-mcp")


@mcp.tool()
def get_current_time() -> str:
    """現在の日本時間（JST）を取得します。
    
    Returns:
        str: YYYY-MM-DD HH:MM:SS JST形式の現在時刻
    """
    # 日本時間（JST）で現在時刻を取得
    jst = ZoneInfo("Asia/Tokyo")
    current_time = datetime.now(jst)
    
    # フォーマットして返す
    return current_time.strftime("%Y-%m-%d %H:%M:%S JST")


def main():
    """サーバーのエントリーポイント"""
    # FastMCPサーバーを起動
    mcp.run()


if __name__ == "__main__":
    main()