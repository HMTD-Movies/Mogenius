import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://HMTD-Links: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@github.com/HMTD-Links/Mogenius-1 $REPO ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
