from config import app

from flask import request, make_response, jsonify

import requests
import os

WEBHOOK = os.getenv('WEBHOOK')

@app.route('/')
def index():
    return 'test'

@app.route('/groupme', methods=['POST'])
def groupme_message():
    data = request.get_json()
    text = data['text']
    user = data['name']
    body = {"content": user +': '+ text}
    if not WEBHOOK:
        print(WEBHOOK)
    response = requests.post(WEBHOOK, json=body)
    return make_response(body, 200)