from mcp.server import FastMCP

from app.tooling.config import get_config

config = get_config()

mcp = FastMCP(
    "Neo4J MCP",
    host=config.mcp_host,
    port=config.mcp_port,
    debug=config.debug_mode
)
