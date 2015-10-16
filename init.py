from flask import render_template, send_from_directory
from flask.ext.migrate import Migrate
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.login import user_logged_in



from forms import *
from admin import admin
from db import db
from kancolle import User,Role

modules = {
    "migrate": None,
    "security": None,
    "user_datastore": None
}

def init(app):
    # --> Extension setup
    db.init_app(app)
    admin.init_app(app)

    modules["migrate"] = Migrate(app, db)

    modules["user_datastore"] = SQLAlchemyUserDatastore(db, User, Role)
    modules["security"] = Security(app, modules["user_datastore"], confirm_register_form=MyRegisterForm)

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

    # --> Signals
    @user_logged_in.connect_via(app)
    def u_logged_in(sender, user):
        """
        Regenerate the API token every login.
        """
        user.api_token = User.generate_api_token()