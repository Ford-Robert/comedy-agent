from fastmcp import FastMCP

# 1) Instantiate
mcp = FastMCP("ScriptGen")

# 2) Define a tool
@mcp.tool()
def generate_script(topic: str, length_seconds: int) -> str:
    return f"A {length_seconds}-second comedy sketch about {topic}."

# 3) Run it
if __name__ == "__main__":
    mcp.run()   # defaults to streamable-http on port 8000
