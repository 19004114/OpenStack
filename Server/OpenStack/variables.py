import requests
from API import get_token

url = "http://10.18.17.50"

try:
    images = requests.get(url + ":9292/v2.1/images",
                          headers={'content-type': 'application/json',
                                   'X-Auth-Token': get_token.get()
                                   },
                          )
    flavors = requests.get(url + ":8774/v2.1/flavors/detail",
                           headers={'content-type': 'application/json',
                                    'X-Auth-Token': get_token.get()
                                    },
                           )
    instances = requests.get(url + ":8774/v2.1/servers/detail",
                             headers={'content-type': 'application/json',
                                      'X-Auth-Token': get_token.get()
                                      },
                             )
    instances_details = instances.json()
    images_details = images.json()
    flavors_details = flavors.json()
except:
    instances_details = {}
    images_details = {}
    flavors_details = {}