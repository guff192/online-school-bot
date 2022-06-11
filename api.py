from aiohttp import web
import json

import db


async def leaderboard(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.students.select())
        users_data = await cursor.fetchall()

        users_response = [dict(user.items()) for user in users_data]

        return web.Response(text=json.dumps(users_response), status=200, content_type='application/json')

