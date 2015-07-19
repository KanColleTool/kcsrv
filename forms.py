# coding=utf-8
from wtforms import fields, validators
from wtforms_alchemy import model_form_factory
from flask.ext.wtf import Form
from flask.ext.security.forms import ConfirmRegisterForm

from db import *

BaseModelForm = model_form_factory(Form)


class MyRegisterForm(ConfirmRegisterForm):
    nickname = fields.StringField('Nickname', [validators.required()])


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session
