#!/usr/bin/env python3
import os
import hashlib

from flask import render_template, send_from_directory
from flask.ext.migrate import Migrate
from flask.ext.security import Security, SQLAlchemyUserDatastore

from forms import *
from admin import admin
from app import app


# --> Extension setup
db.init_app(app)
admin.init_app(app)

migrate = Migrate(app, db)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=MyRegisterForm)

# --> Register blueprints
from modules.play.play import play

app.register_blueprint(play, url_prefix='/play')

from modules.api.core import api_core

app.register_blueprint(api_core, url_prefix='/kcsapi')

# Declare API v1 blueprints.
from modules.api.v1.user import api_user
from modules.api.v1.actions import api_actions
app.register_blueprint(api_user, url_prefix='/kcsapi')
app.register_blueprint(api_actions, url_prefix='/kcsapi')


# Declare API v2 blueprints.
from modules.api.v2.AdmiralAPI import AdmiralAPIv2
from modules.api.v2.DockAPI import DockAPIv2
app.register_blueprint(AdmiralAPIv2, url_prefix='/api/v2/admiral')
app.register_blueprint(DockAPIv2, url_prefix='/api/v2/docks')

from modules.resources import resources

app.register_blueprint(resources, url_prefix='/kcs')

# --> Base application routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/kcs/<path:path>')
def kcs(path):
    return send_from_directory('kcs', path)


if __name__ == '__main__':
    print("Checking for updated api_start2.json...")
    if not os.path.exists("data/api_start2.json.sha256"):
        update = True
        # Generate SHA256 hash
        h = hashlib.sha256((open('data/api_start2.json').read().encode()))
        with open('data/api_start2.json.sha256', 'w') as f:
            f.write(h.hexdigest())
        print("api_start2 hash file not found - updating database.")
    else:
        h = hashlib.sha256(open('data/api_start2.json').read().encode()).hexdigest()
        h2 = open('data/api_start2.json.sha256').read().replace('\n', '')
        if h2 == h:
            print("DB entries are up to date.")
            update = False
        else:
            print("DB entries differ from api_start2.json. You need to update your database.")
            update = True

    app.run(host='0.0.0.0', debug=True)
