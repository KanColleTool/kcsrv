from flask import render_template, send_from_directory, request, abort, g
from flask.ext.login import user_logged_in
from flask.ext.migrate import Migrate
from flask.ext.security import Security, SQLAlchemyUserDatastore

from admin import admin
from db import User, Role, Admiral
from forms import *
from util import generate_api_token


modules = {
    "migrate": None, "security": None, "user_datastore": None
}

admiral = None


def init(app):
    # --> Extension setup
    db.init_app(app)
    admin.init_app(app)

    modules["migrate"] = Migrate(app, db)

    modules["user_datastore"] = SQLAlchemyUserDatastore(db, User, Role)
    modules["security"] = Security(app, modules["user_datastore"], confirm_register_form=MyRegisterForm)

    # Admiral load on each request


    # --> Register blueprints
    from modules.play.play import play


    app.register_blueprint(play, url_prefix='/play')

    from modules.api.core import api_core


    app.register_blueprint(api_core, url_prefix='/kcsapi')

    # Declare API v1 blueprints.
    from modules.api.v1.user import api_user
    from modules.api.v1.actions import api_actions


    @api_user.before_request
    @api_actions.before_request
    def admiral_load():
        # TODO learn how to do this properly
        # g.admiral = Admiral.query.get(3)
        api_token = request.values.get('api_token', None)
        if api_token is None:
            abort(403)
        user = db.session.query(User).filter(User.api_token == api_token).first()
        if user is None:
            return "Invalid api_token"
        g.admiral = user.admiral if user.admiral else Admiral().create(user)


    app.register_blueprint(api_user, url_prefix='/kcsapi')
    app.register_blueprint(api_actions, url_prefix='/kcsapi')

    """
    # Declare API v2 blueprints.
    from modules.api.v2.AdmiralAPI import AdmiralAPIv2
    from modules.api.v2.DockAPI import DockAPIv2
    app.register_blueprint(AdmiralAPIv2, url_prefix='/api/v2/admiral')
    app.register_blueprint(DockAPIv2, url_prefix='/api/v2/docks')
    """
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
        user.api_token = generate_api_token()
