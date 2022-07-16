import requests
import sys
from datetime import date

h = {
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}
x = requests.head(sys.argv[1], headers=h)
print(x.status_code)


if x.status_code == 200:
   print("Everything is ok here!")
else:
   ##
   ##  Open incident
   ##
   url = "http://YYYYYYYYYYYYYYYYYYYYYYYYYYYYY/api/v1/incidents"
   payload = {
       "visible": 1,
       "notify": True,
       "name": sys.argv[1],
       "message": "Our team is working on the issue, we'll come back with an update as soon as possible.",
       "status": 1
   }
   headers = {"Accept": "application/json", "Content-Type": "application/json", "X-Cachet-Application": "Qadisha", "X-Cachet-Token": "XXXXXXXXXXXXXXXXXXX"}
   response = requests.post(url, json=payload, headers=headers)
   print(response.text)
