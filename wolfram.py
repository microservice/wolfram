import os
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--method', help='The http method')
parser.add_argument('--endpoint', help='An endpoint from http://products.wolframalpha.com/api/ must be supplied.'
                                       'Only the endpoints with url api.wolframalpha.com are supported.'
                                       'You do not need to provide your API key via query param as it will be'
                                       'supplied via your environment variable')

args = parser.parse_args()


if args.method is None or args.endpoint is None:
    print({'error': 'must provide a method and an endpoint as named arguments'})
    exit(1)

url = 'https://api.wolframalpha.com' + args.endpoint + '&appid=' + os.environ['WOLFRAM_API_KEY'] + '&output=json'

if args.method == 'get':
    print(requests.get(url).text)
else:
    print({'error': 'method must be one of: get'})
    exit(1)

