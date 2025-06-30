from fastmcp import FastMCP

mcp = FastMCP(name="PS Music")

print("server started:"+mcp.name)

@mcp.tool
def hello(name: str) -> str:
    """ Function that greets the user to my MCP music Server"""
    return "Hello, "+ name +". Welcome to my first MCP Server!"

if __name__ == "__main__":
    # Start the server
    # The server will keep running until interrupted
    # You can access the server at http://localhost:8001
    mcp.run(
        transport="http",
        port=8000,
        )
    print("Server is running...")  
