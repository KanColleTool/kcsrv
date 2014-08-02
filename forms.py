# coding=utf-8
from flask.ext.wtf import Form
from flask.ext.security import current_user
from flask.ext.security.utils import verify_password
from wtforms_alchemy import model_form_factory, ModelFieldList
from wtforms import fields, validators, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from db import *

BaseModelForm = model_form_factory(Form)

class ModelForm(BaseModelForm):
	@classmethod
	def get_session(self):
		return db.session

class AdmiralForm(ModelForm):
	class Meta:
		model = Admiral
		include = ['nickname']
