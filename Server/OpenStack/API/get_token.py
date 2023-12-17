import requests
import json

def get():
    payload = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": "admin",
                        "domain": {
                            "name": "Default"
                        },
                        "password": "123"
                    }
                }
            }
        }
    }
    url = "http://10.18.17.50"
    try:
        res = requests.post(url + ":5000/v3/auth/tokens",
                            headers={'content-type': 'application/json'},
                            data=json.dumps(payload))
    except:
        return ""
    return res.headers['X-Subject-Token']