import requests
from API import get_token

url = "http://192.168.1.8/"

try:
    images = requests.get(url + "compute/v2.1/images",
                        headers = {'content-type' : 'application/json',
                                   'X-Auth-Token' : get_token.get()
                                   },
                        )
    images_details = images.json()

    instances = requests.get(url + "compute/v2.1/servers/detail",
                             headers={'content-type': 'application/json',
                                      'X-Auth-Token': get_token.get()
                                      },
                             )
    instances_details = instances.json()
except:
    images_details = {}
    instances_details = {}