from aiohttp import ClientSession

from settings import API_URL


async def client_session(app):
    app['client'] = ClientSession()
    yield
    await app['client'].close()


async def send_message(msg, client):
    headers = {
        'Content-Type': 'application/json'
    }

    async with client.post(API_URL,
            json=msg,
            headers=headers, ssl=True) as response:
        assert response.status == 200

