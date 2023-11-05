import requests
import json
from API import get_token

payload = {
    "keypair": {
        "name": "test",
    }
}

url = "http://192.168.1.8/"
res = requests.post(url + "compute/v2.1/os-keypairs",
                    headers = {'content-type' : 'application/json',
                               'X-Auth-Token' : get_token.get()},
                    data = json.dumps(payload))

print(res.text)