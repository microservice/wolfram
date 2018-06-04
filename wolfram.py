import os
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--endpoint', help='TODO')

args = parser.parse_args()


if args.endpoint is None:
    print({'error': 'must provide an endpoint as named arguments'})
    exit(1)

url = 'https://api.wolframalpha.com' + args.endpoint + '&appid=' + os.environ['WOLFRAM_API_KEY'] + '&output=json'

print(requests.get(url).text)
