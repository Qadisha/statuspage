import requests
import sys 

h = {
    ...
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}
x = requests.head(sys.argv[1], headers=h)
print(x.status_code)


if x.status_code == 200:
   ##
   ##  Update component status
   ##
   url = "http://YYYYYYYYYYYYYYYYYYYYYYYYYYYYY/api/v1/components/" + sys.argv[2]
   headers = {"Accept": "application/json", "Content-Type": "application/json", "X-Cachet-Application": "Qadisha", "X-Cachet-Token": "XXXXXXXXXXXXXXXXXXX"}
   dataj = {
       "order": 0,
       "group_id": sys.argv[3],
       "enabled": True,
       "status": 1
   }
   response = requests.put(url, headers=headers, json=dataj)
   print(response.text)
   print(dataj)
else:
   ##
   ##  Update component status
   ##
   url = "http://YYYYYYYYYYYYYYYYYYYYYYYYYYYYY/api/v1/components/" + sys.argv[2]
   headers = {"Accept": "application/json", "Content-Type": "application/json", "X-Cachet-Application": "Qadisha", "X-Cachet-Token": "XXXXXXXXXXXXXXXXXXX"}
   dataj = {
       "order": 0,
       "group_id": sys.argv[3],
       "enabled": True,
       "status": 4
   }
   response = requests.put(url, headers=headers, json=dataj)
   print(response.text)
   print(dataj)

