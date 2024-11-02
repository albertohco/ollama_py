import asyncio
from ollama import AsyncClient


async def chat():
    """
    Stream a chat from Llama using the AsyncClient.
    """
    message = {
        "role": "user",
        "content": "Como usar o api no python?"
    }
    async for part in await AsyncClient().chat(
        model="llama3.2", messages=[message], stream=True
    ):
        print(part["message"]["content"], end="", flush=True)


asyncio.run(chat())
