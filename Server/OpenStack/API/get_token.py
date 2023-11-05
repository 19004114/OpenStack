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
                        "password": "minh"
                    }
                }
            }
        }
    }
    url = "http://192.168.1.8/"
    try:
        res = requests.post(url + "identity/v3/auth/tokens",
                            headers={'content-type': 'application/json'},
                            data=json.dumps(payload))
    except:
        return ""
    return res.headers['X-Subject-Token']