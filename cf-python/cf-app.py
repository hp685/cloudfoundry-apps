"""Cloud Foundry test"""
from flask import Flask, jsonify, send_file
import os
import json
import requests

app = Flask(__name__)

URL = "http://appd-configuration-server.apps.hiddenhills.cf-app.com/downloads/AppDynamics-DotNetCore-linux-x64-4.5.18.1.zip"

@app.route('/')
def getenv():
    print("printing appdynamics environment exposed to application")
    appd_env = {"appdynamics_env": { env: os.environ[env] for env in os.environ if env.startswith('APPD')}}
    return jsonify(appd_env)

@app.route('/forward')
def forward():
    response = requests.get(URL, allow_redirects=True)
    with open('agent.zip', 'wb') as f:
        f.write(response.content)
    return send_file('agent.zip', mimetype='application/zip', as_attachment=True, attachment_filename='agent.zip')
