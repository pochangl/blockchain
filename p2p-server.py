import websockets
import asyncio
import argparse

parser = argparse.ArgumentParser(description='Miner process')
parser.add_argument('port', type=int, default=5000, help='port number')

args = parser.parse_args()


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, "localhost", args.port):
        await asyncio.Future()  # run forever

asyncio.run(main())
