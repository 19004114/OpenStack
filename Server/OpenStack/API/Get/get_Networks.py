import requests
import json
from API import get_token

url = "http://192.168.1.8"
res = requests.get(url + ":9696/networking/v2.0/networks",
                    headers = {'content-type' : 'application/json',
                               'X-Auth-Token' : get_token.get()
                               },
                    )

print(res.text)