import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import init

app = Flask(__name__)

if not os.path.exists('./config.py'):
    print("Config file does not exist. You must copy config.example.py to config.py and change the values.")
    exit(1)

app.config.from_object('config_default')
app.config.from_object('config')

# Check config files
if not "SECURITY_PASSWORD_SALT" in app.config or app.config["SECURITY_PASSWORD_SALT"] == "":
    print("Security salt has not been set. Please edit config.py.")

init.init(app)

db = SQLAlchemy()
