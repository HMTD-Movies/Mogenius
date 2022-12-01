import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://HMTD-Links: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@github.com/HMTD-Links/Mogenius-1 $REPO ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
