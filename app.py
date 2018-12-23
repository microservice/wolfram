# -*- coding: utf-8 -*-
import json
import os
import requests
import urllib.parse

from flask import Flask, make_response, request

class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
        self.app_id = os.getenv('WOLFRAM_APP_ID')


    def make_short_answer(self):
        req = request.get_json()
        query = {'i': req['query']}
        encoded_query = urllib.parse.urlencode(query)
        try:
            units = req['units']
        except:
            units = "metric"

        url = f'http://api.wolframalpha.com/v1/result?appid={self.app_id}&{encoded_query}%3f&units={units}'
        response = requests.get(url)

        return self.end({'success': True, 'answer': response.text})


    @staticmethod
    def end(res):
        resp = make_response(json.dumps(res))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp


    @staticmethod
    def app_error(e):
        return json.dumps({'success': False, 'code': 400, 'error': str(e)}), 400


if __name__ == '__main__':
    for env_var in ["WOLFRAM_APP_ID"]:
        assert env_var in os.environ, \
            f"The environment variable '{env_var}' must be set."

    handler = Handler()
    handler.app.register_error_handler(Exception, handler.app_error)
    handler.app.add_url_rule('/shortanswer', 'shortanswer', handler.make_short_answer, methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)

