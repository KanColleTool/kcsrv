import logging
import os

from flask import Flask

import init

__version__ = "0.2.0 Ship Building Simulator 2016 Edition"

app = Flask(__name__)


formatter = logging.Formatter('%(asctime)s - [%(levelname)s] %(name)s -> %(message)s')
root = logging.getLogger()
root.setLevel(app.config.get("LOG_LEVEL", logging.INFO))
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
root.addHandler(consoleHandler)

logger = logging.getLogger("kcsrv")

if not os.path.exists('./config.py'):
    print("Config file does not exist. You must copy config.example.py to config.py and change the values.")
    exit(1)

app.config.from_object('config_default')
app.config.from_object('config')

# Check config files
if not "SECURITY_PASSWORD_SALT" in app.config or app.config["SECURITY_PASSWORD_SALT"] == "":
    print("Security salt has not been set. Please edit config.py.")

# Override encoding.
#import sys
#import codecs
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)

logger.info("Kan'tColle Server {} starting...".format(__version__))

init.init(app)
