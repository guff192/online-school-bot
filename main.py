import logging
from aiohttp import web
import asyncio

from settings import WEBAPP_HOST, WEBAPP_PORT
from client import client_session
from db import pg_context

from bot import message_handler
from api import leaderboard


# Configure logging
logging.basicConfig(level=logging.INFO)


async def init_app(*args):
    app = web.Application()

    # setup routes
    app.add_routes([web.static('/static', './static'),
        web.post('/webhook', message_handler),
        web.get('/leaderboard', leaderboard)])

    # setup client session
    app.cleanup_ctx.append(client_session)

    # setup db
    app.cleanup_ctx.append(pg_context)

    return app


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    try:
        app = init_app(loop)
        web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
    except Exception as e:
        logging.error(f'Error running server: {e}')


