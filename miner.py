from aiohttp import web
import argparse
from blockchain import Blockchain

parser = argparse.ArgumentParser(description='Miner process')
parser.add_argument('port', type=int, help='port number')

args = parser.parse_args()

blockchain = Blockchain()


async def get_blocks(request):
    return web.json_response(data=blockchain.serialize())


app = web.Application()
app.add_routes([web.get('/blocks', get_blocks)])


web.run_app(app, port=args.port)
