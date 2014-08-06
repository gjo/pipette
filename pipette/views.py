# -*- coding: utf-8 -*-

from pyramid.view import view_config


@view_config(route_name='root', renderer='templates/root.pt')
def root(request):
    return {'project': 'pipette'}
