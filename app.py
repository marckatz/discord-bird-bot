from config import app

from flask import request, make_response, jsonify

from dotenv import load_dotenv
import requests
import os

load_dotenv()
WEBHOOK = os.getenv('WEBHOOK')

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return 'test'
    if request.method == 'POST':
        if request.json["type"] == 1:
            return jsonify({
                "type": 1
            })

@app.route('/groupme', methods=['POST'])
def groupme_message():
    data = request.get_json()
    text = data['text']
    user = data['name']
    body = {"content": user +': '+ text}
    response = requests.post(WEBHOOK, json=body)
    return make_response(body, 200)