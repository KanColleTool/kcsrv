# coding=utf-8
from flask.ext.wtf import Form
from wtforms_alchemy import model_form_factory
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
