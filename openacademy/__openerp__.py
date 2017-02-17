# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': "This is a test module",

    'description': """
        This module is to learn how to create a new module and to test if it is recogniced by odoo
    """,

    'author': "Luis González <lgonzalez@vauxoo.com>",
    'website': "http://www.vauxoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ] ,

    'installable': True,
}
