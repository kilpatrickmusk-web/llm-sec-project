from .commanroute import register_routes
from .apiroute import register_api_route


def register_all_routes(app):
    '''register all routes'''
    register_routes(app)
    register_api_route(app)