# -*- coding: utf-8 -*-
import json
import os
import sys
import requests

from flask import Flask, make_response, request


class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
    	self.app_id = os.getenv('APP_ID')

    def makeShortAnswer(self):
    	req = request.get_json()
    	query = req['query']
    	try:
    		units = req['units']
    	except Exception as e:
    		units = ""
    	
    	url = "http://api.wolframalpha.com/v1/result?appid={0}&i={1}%3f&units={2}".format(self.app_id, query, units)
    	response = requests.get(url)

    	return self.end({'response': response.text})

    def end(self, res):
        resp = make_response(json.dumps(res))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp


if __name__ == '__main__':
    if os.getenv('APP_ID') is None:
        print('Environment variable APP_ID not found.')
        sys.exit(1)

    handler = Handler()
    handler.app.add_url_rule('/shortanswer', 'shortanswer', handler.makeShortAnswer , methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)