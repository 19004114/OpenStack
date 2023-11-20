import requests
import json
from API import get_token

url = "http://10.18.17.50"

payload = {
        "server": {
            "name": "Máy",
            "imageRef": "a6e666a3-f454-4025-9fa9-2209f54f4200",
            "flavorRef": "01f95d4c-dfb7-4360-a99b-d11c4e6d8e93",
            "networks": [{
                "uuid": "b1099533-bdfc-45d3-bf76-4cdd3d5db342"
            }],
            "max_count": "3"
        }
    }

res = requests.post(url + ":8774/v2.1/servers",
                    headers={'content-type': 'application/json',
                             'X-Auth-Token': get_token.get()},
                    data=json.dumps(payload)
                    )