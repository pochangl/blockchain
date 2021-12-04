import asyncio
import contextlib
import errno
import json
import socket
import aiohttp
from aiohttp import web, WSMessage
from blockchain import Blockchain

blockchain = Blockchain()


async def get_blocks(request):
    return web.json_response(data=blockchain.serialize())


async def post_mine(request: web.Request):
    json = await request.json()
    data = json['data']
    blockchain.add_block(data)
    loop = asyncio.get_event_loop()
    syncAllChain()
    return web.HTTPTemporaryRedirect('/blocks')


sockets = []
ports = []


async def syncChain(ws: web.WebSocketResponse):
    await ws.send_json(dict(type='blocks', data=blockchain.serialize()))


def syncAllChain():
    loop  = asyncio.get_event_loop()
    for socket in sockets:
        loop.create_task(syncChain(socket))


async def get_messages(ws: web.WebSocketResponse):
    while True:
        msg = await ws.receive()
        if msg.type == aiohttp.WSMsgType.text:
            yield msg
        elif msg.type == aiohttp.WSMsgType.closed:
            break
        elif msg.type == aiohttp.WSMsgType.error:
            break


async def process_message(ws: web.WebSocketResponse, message: WSMessage):
    content = json.loads(message.data)
    print(content)
    if content['type'] == 'sync':
        await syncChain(ws)
    elif content['type'] == 'blocks':
        newblock = Blockchain(content['data'])
        blockchain.replace_chain(newblock)


async def websocketHandler(request: web.Request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    sockets.append(ws)

    async for message in get_messages(ws):
        await process_message(ws, message)

    try:
        sockets.remove(ws)
    except ValueError:
        pass
    print('connection closed: ', ws)


async def connectPeer(port):
    async with aiohttp.ClientSession() as session:
        try:
            ws = await session.ws_connect('http://localhost:{port}/ws'.format(port=port))
        except:
            ports.append(port)
            return

        sockets.append(ws)
        await ws.send_json(dict(type='sync'))
        async for message in get_messages(ws):
            await process_message(ws, message)

        try:
            sockets.remove(ws)
        except ValueError:
            pass
    print('connecion closed', ws)


def main():
    app = web.Application()
    app.add_routes([
        web.get('/blocks', get_blocks),
        web.post('/mine', post_mine),
        web.get('/ws', websocketHandler),
    ])
    app.add_routes([])

    loop = asyncio.get_event_loop()

    for peer_port in range(3000, 3010):
        loop.create_task(connectPeer(peer_port))

    loop.run_until_complete(asyncio.sleep(1))

    web.run_app(app, port=min(ports))


main()
