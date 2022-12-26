import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://HMTD-Movies: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@github.com/HMTD-Movies/Force-Subscribers-Bot $REPO okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 fsubbot.py &")
