import requests
import json

s = requests.Session()

s.headers.update({
	'Authorization': 'Bearer YuD-kWBROOg27DhYlJUnEwY-Z-MQcVH4c.l2USSyKx8EXT8kBcX6oXPXz.6k5EGxpKFS6Iktw5uTJKypOFEdvs376jxOopJD0onhTqD4CzdjaA0WOStbaOj7250s5z13',
	'Content-Type': 'application/json'
})

##url = "https://api.surveymonkey.com/v3/surveys"
url = "https://api.surveymonkey.com/v3/collectors/246369898/responses"

payload = {
	"pages": [{"id": "95299687","questions": [{"answers": [{"choice_id": "2272084645"}], "id": "343960285"}]}]
}

s.post(url, json=payload)

r = s.post(url, json=payload)

print(r.text)