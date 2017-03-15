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
    'depends': [
        'base',
        'purchase',
    ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy_course_view.xml',
        'views/openacademy_session_view.xml',
        'views/openacademy_wizard_view.xml',
        'views/partner.xml',
        'reports/openacademy_session_report.xml',
        'workflows/openacademy_session.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/openacademy_course_demo.xml',
    ],

    'installable': True,
}
