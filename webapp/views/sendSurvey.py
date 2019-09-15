import requests
import json


def send_survey(color):
	s = requests.Session()

	s.headers.update({
		'Authorization': 'Bearer 3ftjpb3cHd1U1myNUT.JRv4Mop8EL5Ux6l6rZ2.COGwou8IYQSPDwGQHvGLVrsxUXpRg1FDYqBnZ8dV6.kmKnnnQpzCmvkECaS-DHyJ1FNnZdlPbn2G3IoIbcHeCNHxz',
		'Content-Type': 'application/json'
	})

	##url = "https://api.surveymonkey.com/v3/surveys"
	url = "https://api.surveymonkey.com/v3/collectors/246392036/responses"

	if(color is "red"):
		payload = {
		"pages": [{"id": "95357896", "questions": [{"answers": [{"choice_id": "2273144661"}], "id": "344117296"}]}]
		}
	else:
		payload = {
		"pages": [{"id": "95357896", "questions": [{"answers": [{"choice_id": "2273144660"}], "id": "344117296"}]}]
		}

	s.post(url, json=payload)
	
	print("Survey sent")
	##r = s.post(url, json=payload)
	##print(r.text)
