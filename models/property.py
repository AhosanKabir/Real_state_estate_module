# -*- coding: utf-8 -*- 
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Property(models.Model):
	_name = 'property'

	name = fields.Char(required = 1 , default='Property') 
	description = fields.Text()
	postcode = fields.Char(required = 1)
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

	state = fields.Selection([
		('draft', 'Draft'),
		('pending', 'Pending'),
		('sold', 'Sold'),
	])

	owner_id = fields.Many2one('owner')

	_sql_constraints = [
		('unique_name', 'unique("name")', 'This name is exist!')
	]

	@api.constrains('bedrooms')
	def _check_bedrooms_greater_zero(self):
		for rec in self:
			if rec.bedrooms == 0:
				# print("not valid") , this is for terminal view 
				raise ValidationError("Please add numbers of bedrooms!")

	# ---------------------------------------- Action Methods -------------------------------------
			
	def action_draft(self):
		for rec in self:
			rec.state = 'draft'

	def action_pending(self):
		for rec in self:
			rec.state = 'pending'
	
	def action_sold(self):
		for rec in self:
			rec.state = 'sold'

	# ---------------------------------------- CRUD -------------------------------------
	# @api.model_create_multi
	# def create(self, vals):
	# 	res = super(Property, self).create(vals)
	# 	print('inside create method')
	# 	return res
	
	# @api.model
	# def write(self, vals):
	# 	res = super(Property, self).write(vals)
	# 	print('inside write method')
	# 	return res
	
	# def unlink(self):
	# 	res = super(Property, self).unlink()
	# 	print('inside delete method')
	# 	return res
			

	