from pyramid.view import view_defaults
import requests


@view_defaults(route_name='request_example', renderer='templates/examples/request.jinja2')
class RequestExampleView:

    def __init__(self, request):
        self._request = request

    def get(self):
        return {
            'path_params': self._request.matchdict,
            'query_params': self._request.params
        }


@view_defaults(route_name='sm_api_example', renderer='templates/examples/sm_api.jinja2')
class SMAPIExampleView:

    def __init__(self, request):
        self._request = request

    def get(self):
        r = requests.get('https://api.surveymonkey.com/v3/surveys?include=collect_url', headers={
                'Authorization': 'bearer {}'.format(self._request.registry.settings.get('sm.key')),
                'Content-Type': 'application/json'
            })
        response = r.json()
        return {
            'surveys': response['data']
        }


def includeme(config):
    # This route will only be matched if variable1 and variable2 are supplied. variable1 must be an integer.
    config.add_route('request_example', '/example/request/{variable1:\d+}/{variable2}')
    config.add_view(RequestExampleView, attr='get', request_method='GET')

    config.add_route('sm_api_example', '/example/sm_api')
    config.add_view(SMAPIExampleView, attr='get', request_method='GET')
