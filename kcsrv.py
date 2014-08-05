#!/usr/bin/env python
from flask import Flask, render_template, send_from_directory
from flask.ext.migrate import Migrate
from flask.ext.security import Security, SQLAlchemyUserDatastore
from db import *
from forms import *
from admin import admin



# --> App setup
app = Flask(__name__)
app.config['DEBUG'] = None
app.config.from_object('config_default')
app.config.from_object('config')



# --> Extension setup
db.init_app(app)
admin.init_app(app)

migrate = Migrate(app, db)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=MyRegisterForm)



# --> Register blueprints
from modules.play.play import play
app.register_blueprint(play, url_prefix='/play')



# --> Base application routes
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/kcs/<path:path>')
def kcs(path):
	return send_from_directory('kcs', path)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
