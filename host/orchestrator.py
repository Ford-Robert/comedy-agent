from fastmcp import FastMCPClient

client = FastMCPClient("http://localhost:8000/rpc")
script = await client.call("generate_script", {"topic": "cats", "length_seconds": 30})
