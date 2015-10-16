from flask.ext.admin import Admin, AdminIndexView, BaseView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security import current_user
from wtforms import fields

from kancolle import db,auth
from kancolle.admiral import Admiral
from kancolle.navalbase import Recipe


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
    form_overrides = {'description': fields.TextAreaField}


class UserModelView(MyModelView):
    column_exclude_list = ['password']
    form_excluded_columns = ['password']


class AdmiralModelView(MyModelView):
    column_exclude_list = ['tutorial_progress', 'max_furniture', 'furniture', 'furniture_coins', 'max_ships', 'max_equips',
                           'available_fleets', 'available_cdocks', 'available_rdocks',
                           'sortie_successes', 'sortie_total', 'expedition_successes', 'expedition_total',
                           'pvp_successes', 'pvp_total', 'resources', 'setup']

class RecipeModelView(MyModelView):
    pass


admin = Admin(index_view=MyAdminIndexView())
admin.add_view(RoleModelView(auth.Role, db.session, endpoint='role'))
admin.add_view(UserModelView(auth.User, db.session, endpoint='user'))
admin.add_view(AdmiralModelView(Admiral, db.session, endpoint='admiral'))
admin.add_view(RecipeModelView(Recipe, db.session, endpoint='recipes'))
