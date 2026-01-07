from fastmcp import Client
from openai import OpenAI
import asyncio
import os
import json

f = open(os.path.dirname(__file__) + "/secret_key.txt")
key = f.readline()

openai_client = OpenAI(api_key=key)

class Agent:
    """
    The class Agent is used for the PokeChat application. The logic is defined in the
    logic function.

    Usage:
    - Have a valid api key to openai in the secret_key.txt file
    - Make a class instance
    - Use the class function "logic" to run through the agent its logic.
    """
    def __init__(self):
        self.client = Client("http://server:80/api/mcp")

    async def logic(self, message: str) -> str:
        """
        Main agent loop:
        1. Discover MCP tools
        2. Give tools to OpenAI
        3. Let OpenAI choose a tool + arguments
        4. Call MCP tool
        5. Send result back to OpenAI for final answer
        """

        async with self.client:
            mcp_tools = await self.client.list_tools()

        openai_tools = []
    
        for tool in mcp_tools:
            openai_tools.append({
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description or "",
                    "parameters": tool.inputSchema
                }
            })

        response = openai_client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Pokémon expert. Use tools when needed."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            tools=openai_tools,
            tool_choice="auto"
        )

        assistant_message = response.choices[0].message

        # If OpenAI does not return a tool, then return its text
        if not assistant_message.tool_calls:
            return assistant_message.content

        tool_call = assistant_message.tool_calls[0]
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        async with self.client:
            tool_result = await self.client.call_tool(tool_name, arguments)

        followup = openai_client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": message},
                {
                    "role": "assistant",
                    "tool_calls": assistant_message.tool_calls
                },
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(tool_result)
                }
            ]
        )

        return followup.choices[0].message.content
