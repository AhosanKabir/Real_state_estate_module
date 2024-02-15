# -*- coding: utf-8 -*- 
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class Property(models.Model):
	_name = 'property'
	_inherit = ['mail.thread','mail.activity.mixin']

	name = fields.Char(required = 1 , default='Property') 
	description = fields.Text()
	active = fields.Boolean( default = True)
	postcode = fields.Char(required = 1)
	date_availability = fields.Date(tracking = 1)
	expected_price = fields.Float()
	selling_price = fields.Float()
	diff = fields.Float(compute= "_compute_diff" , store=1)
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

	# explore related fields in odoo (bottom ):
	owner_address = fields.Char(related='owner_id.address')
	owner_phone = fields.Char(related='owner_id.phone', size=11)

	_sql_constraints = [
		('unique_name', 'unique("name")', 'This name is exist!')
	]

	@api.depends('expected_price', 'selling_price') 
	def _compute_diff(self):
		for rec in self:
			rec.diff = rec.expected_price - rec.selling_price


	@api.onchange('expected_price')
	def _onchange_expected_price(self):
		for rec in self:
			rec._check_expected_price()
			# raise UserError("This is an error message.")
			return {
				'warning': {
					'title': 'warning',
					'message': 'please input positive value.',
					'type': 'notification'
				}
			}

	# @api.depends('expected_price')
	def _check_expected_price(self):
		for rec in self:
			if rec.expected_price < 0:
				rec.expected_price = rec.expected_price * (-1)


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
			

	