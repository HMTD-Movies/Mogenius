import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://HMTD-Movies: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@github.com/HMTD-Movies/Mogenius $REPO ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
