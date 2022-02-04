import requests
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Success"

@app.route('/api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    url = data["url"]
    payload = data["body"]
    headers = {'content-type': "application/json"}
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    # print(type(response.text))
    return response.text

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 8080 ,debug=False)