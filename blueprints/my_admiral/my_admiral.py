from flask import Blueprint, render_template

my_admiral = Blueprint('my_admiral', __name__, template_folder='templates')

@my_admiral.route('/')
def index():
	return render_template('my_admiral/index.html')
