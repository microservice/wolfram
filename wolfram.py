import os
import sys
import json
import requests

endpoint = json.loads(sys.argv[2])['endpoint']

url = 'https://api.wolframalpha.com' + endpoint + '&appid=' + os.environ['WOLFRAM_API_KEY'] + '&output=json'

if sys.argv[1] == 'get':
    print(requests.get(url).text)
else:
    print({'error': 'method must be one of: get'})
    exit(1)

