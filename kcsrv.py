#!/usr/bin/env python
from flask import Flask, render_template
from flask.ext.migrate import Migrate
from flask.ext.security import Security, SQLAlchemyUserDatastore
from db import *
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
security = Security(app, user_datastore)



# --> Register blueprints
from blueprints.my_admiral.my_admiral import my_admiral
app.register_blueprint(my_admiral, url_prefix='/admiral')



# --> Base application routes
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
