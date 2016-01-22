from flask.ext.admin import Admin, AdminIndexView, BaseView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security import current_user
from wtforms import fields
from db import db, User, Role, Recipe, RecipeResources, Admiral, Kanmusu, Equipment, Fleet


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

    inline_models = (Admiral,)


class AdmiralModelView(MyModelView):
    column_exclude_list = ['tutorial_progress', 'max_furniture', 'furniture', 'furniture_coins', 'max_ships',
                           'max_equips', 'available_fleets', 'available_cdocks', 'available_rdocks', 'sortie_successes',
                           'sortie_total',
                           'expedition_successes', 'expedition_total', 'pvp_successes', 'pvp_total', 'setup']


admin = Admin(index_view=MyAdminIndexView(), template_mode='bootstrap3')
admin.add_view(RoleModelView(Role, db.session, endpoint='role'))
admin.add_view(UserModelView(User, db.session, endpoint='user'))
admin.add_view(AdmiralModelView(Admiral, db.session, endpoint='admiral'))
admin.add_view(MyModelView(Kanmusu, db.session, endpoint='shipgirl'))
admin.add_view(MyModelView(Recipe, db.session, endpoint='recipe'))
admin.add_view(MyModelView(RecipeResources, db.session, endpoint='rr'))
admin.add_view(MyModelView(Equipment, db.session, endpoint='equip'))
admin.add_view(MyModelView(Fleet, db.session, endpoint='fleet'))
