from aiohttp import web
import argparse
from blockchain import Blockchain

parser = argparse.ArgumentParser(description='Miner process')
parser.add_argument('port', type=int, default=3000, help='port number')

args = parser.parse_args()

blockchain = Blockchain()


async def get_blocks(request):
    return web.json_response(data=blockchain.serialize())


async def post_mine(request: web.Request):
    json = await request.json()
    data = json['data']
    blockchain.add_block(data)
    return web.HTTPTemporaryRedirect('/blocks')

app = web.Application()
app.add_routes([web.get('/blocks', get_blocks)])
app.add_routes([web.post('/mine', post_mine)])


web.run_app(app, port=args.port)
