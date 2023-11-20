import requests
import json
from API import get_token

url = "http://192.168.1.8/"
res = requests.get(url + "compute/v2.1/images",
                    headers = {'content-type' : 'application/json',
                               'X-Auth-Token' : get_token.get()
                               },
                    )

data = res.json()
value = data['images'][1]['id']
count = len(data['images'])

imageList = {}

for i in range(count):
    if data['images'][i]['id'] not in imageList.keys():
        imageList[data['images'][i]['id']] = data['images'][i]['name']

print(data['images'])