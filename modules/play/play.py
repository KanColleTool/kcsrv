from flask import Blueprint, request, url_for, render_template
from flask import redirect
from flask.ext.security import current_user, AnonymousUser

play = Blueprint('play', __name__, template_folder='templates')


@play.route('/')
def index():
    if hasattr(current_user, 'api_token'):
        api_token = current_user.api_token
        return render_template('play/index.html', api_token=api_token)
    else:
        return redirect('/account/login')
