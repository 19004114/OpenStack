import requests
import json

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
                        headers = {'content-type' : 'application/json'},
                        data = json.dumps(payload))
except:
    res = []

def get():
    return res.headers['X-Subject-Token']