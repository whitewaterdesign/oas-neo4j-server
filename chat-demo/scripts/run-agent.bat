@echo off
REM Navigate to the agent directory
cd /d %~dp0\..\..

REM Run the agent using uv
uv run -m app.agent_os
