
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = None
app.config.from_object('config_default')
app.config.from_object('config')