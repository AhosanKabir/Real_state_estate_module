# -*- coding: utf-8 -*-
{
    'name': "estate",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Estate Property business system 
    """,

    'author': "Ahosan",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
		'views/base_menu.xml',
		'views/property_view.xml',
		'views/owner_view.xml',
		'views/sale_order_view.xml',
		'views/building_view.xml',
		'reports/property_report.xml',
    ],
	
    'assets':{
		'web.assets_backend':[
			'/estate/static/src/css/style.css',
        ]
    },

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
	
    'sequence':1,
	'installable':True,
	'application':True
}