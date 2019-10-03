import json

import requests

#POST requests have everything a GET request had + json or XML

headers = {'Content-Type': 'application/json'}

path = 'http://api.postcodes.io/postcodes/'

arguments = ''

json_body = json.dumps({"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]})

multi_post_codes = requests.post(path, headers = headers, data = json_body)

print(multi_post_codes.json())

