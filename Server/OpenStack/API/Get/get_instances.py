import requests
import json
from API import get_token

url = "http://192.168.1.8/"
res = requests.get(url + "compute/v2.1/servers/detail",
                    headers = {'content-type' : 'application/json',
                               'X-Auth-Token' : get_token.get()
                               },
                    )

data = res.json()
value = data['servers'][0]['name']
print(data['servers'][0])

for i in data['servers']:
    print(i['name'])
    print(i['OS-EXT-STS:power_state'])
    print(i['addresses']['public'][0]['addr'])