import requests
import json
from API import get_token

url = "http://10.18.17.50"
res = requests.get(url + ":8774/v2.1/flavors/detail",
                    headers = {'content-type' : 'application/json',
                               'X-Auth-Token' : get_token.get()
                               },
                    )
data = res.json()
print(data['flavors'])