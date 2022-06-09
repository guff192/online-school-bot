import logging
import asyncio
import aiohttp
from aiohttp import web

from settings import WEBAPP_HOST, WEBAPP_PORT
from bot import message_handler
from client import client_session

# Configure logging
logging.basicConfig(level=logging.INFO)


async def init_app(loop):
    app = web.Application()
    app.add_routes([web.static('/static', './static'),
        web.post('/webhook', message_handler)])
    app['client'] = aiohttp.ClientSession()
    app.cleanup_ctx.append(client_session)
    return app


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    try:
        app = init_app(loop)
        web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
    except Exception as e:
        logging.error(f'Error running server: {e}')


