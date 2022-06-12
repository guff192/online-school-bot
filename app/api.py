from aiohttp import web
import simplejson

from db import get_students_list


async def leaderboard(request):
    async with request.app['db'].acquire() as conn:
        users_data = await get_students_list(conn)

        users_response = [dict(user) for user in users_data]

        return web.Response(text=simplejson.dumps(users_response), status=200, content_type='application/json')

