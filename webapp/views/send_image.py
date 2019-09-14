from pyramid.view import view_defaults
import requests
import json
from base64 import b64decode
import string
import random

@view_defaults(route_name='send_image', renderer='json')
class SendImageView:
    def __init__(self, request):
        self._request = request

    def post(self):
        img = self._request.headers['img']
        print((self._request.headers['img']))
        # print(json.loads(self._request))
        header, encoded = img.split(",", 1)
        data = b64decode(encoded)
        with open("images/data/ours-up/" + ''.join(random.choice(string.ascii_lowercase) for i in range(12)) + ".png", "wb") as f:
            f.write(data)
        return 'thumbup/down'


def includeme(config):
    config.add_route('send_image', '/send_image')
    config.add_view(SendImageView, attr='post', request_method="POST")
