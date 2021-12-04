import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://localhost:5000") as websocket:
        while True:
            ipt = input()
            await websocket.send(ipt)
            print(await websocket.recv())

asyncio.run(hello())
