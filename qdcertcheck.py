from urllib.request import ssl, socket
from datetime import datetime, timezone
import OpenSSL
import sys
import requests
import json
import os

def get_num_days_before_expired(hostname: str, port: str = '443') -> int:
    """
    Get number of days before an TLS/SSL of a domain expired
    """
    context = ssl.SSLContext()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname = hostname) as ssock:
            certificate = ssock.getpeercert(True)
            cert = ssl.DER_cert_to_PEM_cert(certificate)
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
            cert_expires = datetime.strptime(x509.get_notAfter().decode('utf-8'), '%Y%m%d%H%M%S%z')
            num_days = (cert_expires - datetime.now(timezone.utc)).days
            print(f'{hostname} expires in {num_days} day(s)')
            return num_days

#if __name__ == '__main__':
#    get_num_days_before_expired('expired-rsa-dv.ssl.com')

num_days = get_num_days_before_expired(sys.argv[1])
if num_days > 0:
   print("Valid certificate")

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

elif num_days == 0:
   print("Expired today")

##
##  Update component status
##

   url = "http://YYYYYYYYYYYYYYYYYYYYYYYYYYYYY/api/v1/components/" + sys.argv[2]
   headers = {"Accept": "application/json", "Content-Type": "application/json", "X-Cachet-Application": "Qadisha", "X-Cachet-Token": "XXXXXXXXXXXXXXXXXXX"}
   dataj = {
     "order": 0,
     "group_id": sys.argv[3],
     "enabled": True,
     "status": 3
   }
   response = requests.put(url, headers=headers, json=dataj)
   print(response)
   print(url)

##
##  Create Incident
##
   url2 = "http://YYYYYYYYYYYYYYYYYYYYYYYYYYYYY/api/v1/incidents"
   headers2 = {"Accept": "application/json", "Content-Type": "application/json", "X-Cachet-Application": "Qadisha", "X-Cachet-Token": "XXXXXXXXXXXXXXXXXXX"}
   dataj2 = {
     "visible": 1,
     "notify": True,
     "name": "SSL certificate issue recorded on " + sys.argv[1],
     "message": "We're experiencing issues with the SSL certificate installed on " + sys.argv[1] + ", our team has been engaged and we're waiting for their feedback." ,
     "status": 1,
     "component_id": sys.argv[2],
     "component_status": 4
   }
   response2 = requests.post(url2, headers=headers2, json=dataj2)
   print(response2)
   print(dataj2)

else:
   print("Expired")

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
   print(response)
   print(url)

##
##  Create Incident
##
   url2 = "http://YYYYYYYYYYYYYYYYYYYYYYYYYYYYY/api/v1/incidents"
   headers2 = {"Accept": "application/json", "Content-Type": "application/json", "X-Cachet-Application": "Qadisha", "X-Cachet-Token": "XXXXXXXXXXXXXXXXXXX"}
   dataj2 = {
     "visible": 1,
     "notify": True,
     "name": "SSL certificate issue recorded on " + sys.argv[1],
     "message": "We're experiencing issues with the SSL certificate installed on " + sys.argv[1] + ", our team has been engaged and we're waiting for their feedback." ,
     "status": 1,
     "component_id": sys.argv[2],
     "component_status": 4
   }
   response2 = requests.post(url2, headers=headers2, json=dataj2)
   print(response2)
   print(dataj2)
