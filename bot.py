from aiohttp import web

from client import send_message


async def message_handler(request):
    data = await request.json()
    message = {
        'chat_id': data['message']['chat']['id'],
        'text': data['message']['text']
    }

    try:
        await send_message(message, request.app['client'])
    except:
        return web.Response(body='Error sending message', status=500)

    return web.Response(status=200)

