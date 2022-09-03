import requests
import sys
from datetime import date

h = {
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}

try:
    x = requests.head(sys.argv[1], headers=h, stream=True, timeout=10)
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


except requests.exceptions.HTTPError as err:
    print("HTTP Error")

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

except requests.exceptions.RequestException as e:
    print("Other Exception")

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