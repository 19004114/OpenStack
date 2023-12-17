import requests
import json
from API import get_token

def create_vm(soluong,image,flavor):
    url = "http://10.18.17.50"
    payload = {
        "server": {
            "name": "Máy",
            "imageRef": image,
            "flavorRef": flavor,
            "networks": [{
                "uuid": "b1099533-bdfc-45d3-bf76-4cdd3d5db342"
            }],
            "max_count": soluong
        }
    }
    res = requests.post(url + ":8774/v2.1/servers",
                        headers={'content-type': 'application/json',
                                 'X-Auth-Token': get_token.get()},
                        data=json.dumps(payload)
                        )
    return res