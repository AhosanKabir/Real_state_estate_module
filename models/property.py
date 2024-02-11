# -*- coding: utf-8 -*- 
from odoo import models, fields, api

class Property(models.Model):
	_name = 'property'

	name = fields.Char()
	description = fields.Text()
	postcode = fields.Char()
	date_availability = fields.Date()
	expected_price = fields.Float()
	selling_price = fields.Float()
	bedrooms = fields.Integer()
	Living_area = fields.Integer() 
	facades = fields.Integer()
	garage = fields.Boolean()
	garden = fields.Boolean()
	garden_area = fields.Integer()
	garden_orientation = fields.Selection([
		('north', 'North'),
		('south', 'South'),
		('east', 'East'),
		('west', 'West'),
	])