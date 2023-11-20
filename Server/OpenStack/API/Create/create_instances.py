import requests
import json
from API import get_token

payload = {
    "server": {
        "name": "test",
        "imageRef": '87399d56-5f8f-481e-b4c9-75a0a090096c',
        "flavorRef": 'c1',
        "networks": [{
            "uuid": "57085e72-e9f0-4305-8e7d-6fe1a9d322d7"
        }]
    }
}

url = "http://192.168.1.8/"
res = requests.post(url + "compute/v2.1/servers",
                    headers = {'content-type' : 'application/json',
                               'X-Auth-Token' : get_token.get()},
                    data = json.dumps(payload)
                    )
print(res.text)