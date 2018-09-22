from aiohttp import web
from aioelasticsearch import Elasticsearch


async def handle(request):
    return web.Response(text=str(await request.app['es'].ping()))


async def make_es(app):
    app['es'] = Elasticsearch()

    yield

    await app['es'].close()


async def make_app():
    app = web.Application()
    app.add_routes([web.get('/', handle)])

    app.cleanup_ctx.append(make_es)

    return app


web.run_app(make_app())
