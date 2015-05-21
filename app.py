import os

from flask import Flask

app = Flask(__name__)

if not os.path.exists('./config.py'):
    print("Config file does not exist. You must copy config.example.py to config.py and change the values.")
    exit(1)

app.config['DEBUG'] = None
app.config.from_object('config_default')
app.config.from_object('config')