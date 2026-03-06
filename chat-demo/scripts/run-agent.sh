#!/bin/bash

# Navigate to the agent directory
cd "$(dirname "$0")/../.." || exit 1

# Run the agent using uv
uv run -m app.agent_os
