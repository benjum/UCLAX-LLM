from mcp.server.fastmcp import FastMCP
mcp = FastMCP("mcp_server")
import subprocess

@mcp.tool()
def current_datetime(timezone):
    return subprocess.check_output(["date", "+%Y-%m-%d %H:%M:%S %Z"], text=True).strip()

if __name__ == "__main__":
    mcp.run(transport="stdio")
