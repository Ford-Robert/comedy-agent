# comedy-agent


I want to build an agentic ai that will automatically produce youtube comedy shorts and upload them to the platform. Later I want the agent to be able to learn from the youtube metrics about how to make better shorts, so as to have a self improving agent.

/mcp-servers
  /script-gen-server
  /media-assemble-server
  /youtube-api-server
  /metrics-ingest-server
/host
  orchestrator.ts      # MCP Host client + orchestration logic
  prompt-templates/    # JSON-RPC method schemas + prompt snippets
/shared
  types/               # TypeScript interfaces for all MCP methods
  utils/