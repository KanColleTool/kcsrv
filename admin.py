from flask.ext.admin import Admin, AdminIndexView, BaseView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security import current_user
from wtforms import fields
from db import *

class AdminAuthMixin(object):
	def is_accessible(self):
		return current_user.has_role('admin')

class MyAdminIndexView(AdminAuthMixin, AdminIndexView):
	pass

class MyBaseView(AdminAuthMixin, BaseView):
	pass

class MyModelView(AdminAuthMixin, ModelView):
	pass



class RoleModelView(MyModelView):
	form_overrides = { 'description': fields.TextAreaField }

class UserModelView(MyModelView):
	column_exclude_list = ['password']
	form_excluded_columns = ['password']

class AdmiralModelView(MyModelView):
	form_excluded_columns = ['versions']



admin = Admin(index_view=MyAdminIndexView())
admin.add_view(RoleModelView(Role, db.session, endpoint='role'))
admin.add_view(UserModelView(User, db.session, endpoint='user'))
admin.add_view(AdmiralModelView(Admiral, db.session, endpoint='admiral'))
