import requests
import json
from API import get_token

payload = {
    "flavor": {
        "name": "test",
        "ram": 1024,
        "vcpus": 2,
        "disk": 10,
        "id": "t1"
    }
}

url = "http://192.168.1.8/"
res = requests.post(url + "compute/v2.1/flavors",
                    headers = {'content-type' : 'application/json',
                               'X-Auth-Token' : get_token.get()},
                    data = json.dumps(payload)
                    )
print(res.text)