from pyramid.view import view_defaults


@view_defaults(route_name='home', renderer='templates/base.jinja2')
class HomeView:

    def __init__(self, request):
        self._request = request

    def get(self):
        return {}


def includeme(config):
    config.add_route('home', '/')
    config.add_view(HomeView, attr='get', request_method='GET')
