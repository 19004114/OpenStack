import requests
import json
from API import get_token

url = "http://10.18.17.50"
res = requests.get(url + ":9292/v2.1/images",
                    headers = {'content-type' : 'application/json',
                               'X-Auth-Token' : get_token.get()
                               },
                    )

data = res.json()
value = data['images'][1]['id']
count = len(data['images'])

print(data['images'][0]['name'])