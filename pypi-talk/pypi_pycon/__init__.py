from pyramid.config import Configurator
from pyramid.response import Response

def ping(request):
    return Response("hello Pyconar!")


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # set pypicloud configurations
    config.include("pypicloud")
    config.scan("pypicloud.views")

    # cuustom view
    config.add_route("ping", "/ping")
    config.add_view(ping, route_name="ping")

    return config.make_wsgi_app()
