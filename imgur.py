import base64
import json
import requests

from base64 import b64encode

client_id = '5d3ce8262b25794'

headers = {"Authorization": "Client-ID 5d3ce8262b25794"}

url = "https://api.imgur.com/3/image"

j1 = requests.post(
    url, 
    headers = headers,
    data = {
        'image': b64encode(open('test.png', 'rb').read()),
        'type': 'base64',
        'name': 'test.png',
        'title': 'Picture'
    }
)
print(j1.json()['data']['link'])

# url = "https://api.imgur.com/3/image/{{imageHash}}"