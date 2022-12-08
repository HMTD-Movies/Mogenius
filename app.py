import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://HMTD-Movies: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@github.com/HMTD-Movies/UK-Movies-Bot $REPO okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
