import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8001/mcp")

async def main():
    async with client:
        # Get the available tools/operations
        tools = await client.list_tools()
        #print("Available tools:", tools)

        # Call the 'hello' tool with a parameter
        response = await client.call_tool("hello", {"name": "Priyatham"})
        print("Response=", response[0].text)



asyncio.run(main())