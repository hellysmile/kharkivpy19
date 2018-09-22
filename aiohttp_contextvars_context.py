import contextvars

from aiohttp import web
from aioelasticsearch import Elasticsearch

ctx = contextvars.ContextVar('es')


async def handle(request):
    return web.Response(text=str(await ctx.get().ping()))


async def make_app():
    app = web.Application()
    app.add_routes([web.get('/', handle)])

    async def close_es(app):
        await ctx.get().close()
    app.on_shutdown.append(close_es)

    return app

ctx.set(Elasticsearch())

web.run_app(make_app())
