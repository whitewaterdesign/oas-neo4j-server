from agno.os import AgentOS
from agno.os.interfaces.agui import AGUI

from app.client.agent import openapi_cypher_agent

# AgentOS manages MCP lifespan
agent_os = AgentOS(
    description="AgentOS with MCP Tools",
    agents=[openapi_cypher_agent],
    interfaces=[AGUI(agent=openapi_cypher_agent)]
)

app = agent_os.get_app()

if __name__ == "__main__":
    # Don't use reload=True with MCP tools to avoid lifespan issues
    agent_os.serve(app="app.agent_os:app", port=8000, reload=True)
