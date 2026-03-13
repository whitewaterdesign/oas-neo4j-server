## Fire up Neo4J

```shell
docker compose up -d
```

## Fire up MCP Server

```shell
uv run python -m app.mcp
```


## Fire up AgentOS

```shell
uv run python -m app.agent_os
```

## Fire up UI

```shell
cd chat-demo
pnpm run dev:ui
```

## Build graph
```shell
uv run python -m app.main
```
