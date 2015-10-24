# coding=utf-8
from flask.ext.security.forms import ConfirmRegisterForm
from flask.ext.wtf import Form
from wtforms import fields, validators
from wtforms_alchemy import model_form_factory

from db import db

BaseModelForm = model_form_factory(Form)

class MyRegisterForm(ConfirmRegisterForm):
    nickname = fields.StringField('Nickname', [validators.required()])

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session
