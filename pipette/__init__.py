# -*- coding: utf-8 -*-

from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('root', '/')
    config.scan()
    return config.make_wsgi_app()
