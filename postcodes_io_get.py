import requests


#GET is a server request that sends:
    # Headers, paths and argumenents
    # Headers are metadata slightly hiddden - things like sceen size, device info, and other
    # Path is the location on the internet -- URL section that determines where to send info
    # Arguments are the information you send

headers = ''
path = 'http://api.postcodes.io/postcodes/'
arguments = 'E146GT'

post_code_req = requests.get(path, arguments)

print(post_code_req)

print(post_code_req.status_code)

print(post_code_req.headers)

print((post_code_req.content))

print(type(post_code_req.json()))



