from flask import Blueprint, render_template, url_for, redirect
from flask.ext.security import current_user
from db import db, Admiral
from forms import AdmiralForm

my_admiral = Blueprint('my_admiral', __name__, template_folder='templates')

@my_admiral.route('/')
def index():
	admiral = current_user.admiral
	if not admiral:
		return redirect(url_for('.create'))
	return render_template('my_admiral/index.html', admiral=admiral)

@my_admiral.route('/create/', methods=['GET', 'POST'])
def create():
	admiral = Admiral()
	form = AdmiralForm(obj=admiral)
	if form.validate_on_submit():
		#form.populate_obj(admiral)
		admiral.nickname = form.nickname.data
		admiral.generate_api_token()
		current_user.admiral = admiral
		db.session.add(admiral)
		db.session.add(current_user)
		db.session.commit()
		return redirect(url_for('.index'))
	return render_template('my_admiral/form.html', admiral=admiral, form=form, creating=True)
