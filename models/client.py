# -*- coding: utf-8 -*- 
from odoo import models, api, fields

class Client(models.Model):
	_name = 'client'
	_inherit = 'owner'