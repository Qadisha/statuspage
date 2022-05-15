import platform
import subprocess
import sys
import requests

def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
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
      return True
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
      return False

myping(sys.argv[1])
