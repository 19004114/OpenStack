import requests
import json
from API import get_token

def get_data():
    url = "http://192.168.1.8/"
    try:
        res = requests.get(url + "container/v1/containers/",
                            headers = {'content-type' : 'application/json',
                                       'X-Auth-Token' : get_token.get()
                                       },
                            )
        data = res.json()
        return data['containers']
    except:
        data = []
        return data