import requests
import json
from API import get_token

url = "http://192.168.1.8/"
res = requests.get(url + "compute/v2.1/flavors",
                    headers = {'content-type' : 'application/json',
                               'X-Auth-Token' : get_token.get()
                               },
                    )

print(res.text)