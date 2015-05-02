# coding=utf-8
from wtforms import fields, validators
from wtforms_alchemy import model_form_factory

from flask.ext.wtf import Form
from flask.ext.security.forms import RegisterForm
from db import *


BaseModelForm = model_form_factory(Form)


class MyRegisterForm(RegisterForm):
    nickname = fields.TextField(u'Nickname', [validators.required()])


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session
