import logging
import os
from dotenv import load_dotenv

import asyncio
import aiohttp
from aiohttp import web

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')
API_URL = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
API_SETWEBHOOK_URL = f'https://api.telegram.org/bot{API_TOKEN}/setWebhook'

# webhook settings
WEBHOOK_HOST = os.environ.get('WEBHOOK_HOST')
WEBHOOK_PATH = '/webhook'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

print(API_TOKEN, WEBHOOK_HOST, sep='\n')

# webserver settings
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 5000

# Configure logging
logging.basicConfig(level=logging.INFO)


async def send_message(msg):
    headers = {
        'Content-Type': 'application/json'
    }

    async with aiohttp.ClientSession() as client:
        logging.info('Successfully started session')
        async with client.post(API_URL,
                json=msg,
                headers=headers, ssl=True) as response:
            logging.info('Got the response')
            assert response.status == 200


async def handler(request):
    data = await request.json()
    message = {
        'chat_id': data['message']['chat']['id'],
        'text': data['message']['text']
    }

    try:
        await send_message(message)
    except:
        return web.Response(body='Error sending message', status=500)

    return web.Response(status=200)


async def init_app(loop):
    app = web.Application()
    app.add_routes([web.static('/static', './static'),
        web.post('/webhook', handler)])
    return app



if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    try:
        app = init_app(loop)
        web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
    except Exception as e:
        logging.error(f'Error running server: {e}')

