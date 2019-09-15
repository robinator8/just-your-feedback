from pyramid.view import view_defaults
import requests
import json
from base64 import b64decode
import string
import random
import sys
# sys.path.append('../../')
from .imagePred import image_pred
# from sendSurvery.py import send_survey

@view_defaults(route_name='send_image', renderer='json')
class SendImageView:
    def __init__(self, request):
        self._request = request

    def post(self):
        img = self._request.headers['img']
        # print((self._request.headers['img']))
        # print(json.loads(self._request))
        header, encoded = img.split(",", 1)
        data = b64decode(encoded)
        color = image_pred(data)
        send_survey(color)
        if color == 'green':
            return 'Survey Submitted! You answered yes! :)'
        else:
            return 'Survey Submitted! You answered no! :('


def includeme(config):
    config.add_route('send_image', '/send_image')
    config.add_view(SendImageView, attr='post', request_method="POST")

def send_survey(color):
	s = requests.Session()

	s.headers.update({
		'Authorization': 'Bearer 3ftjpb3cHd1U1myNUT.JRv4Mop8EL5Ux6l6rZ2.COGwou8IYQSPDwGQHvGLVrsxUXpRg1FDYqBnZ8dV6.kmKnnnQpzCmvkECaS-DHyJ1FNnZdlPbn2G3IoIbcHeCNHxz',
		'Content-Type': 'application/json'
	})

	##url = "https://api.surveymonkey.com/v3/surveys"
	url = "https://api.surveymonkey.com/v3/collectors/246392036/responses"

	if(color == "red"):
		payload = {
		"pages": [{"id": "95357896", "questions": [{"answers": [{"choice_id": "2273144661"}], "id": "344117296"}]}]
		}
		print("red")
	else:
		payload = {
		"pages": [{"id": "95357896", "questions": [{"answers": [{"choice_id": "2273144660"}], "id": "344117296"}]}]
		}

	s.post(url, json=payload)
	
	print("Survey sent")
	##r = s.post(url, json=payload)
	##print(r.text)