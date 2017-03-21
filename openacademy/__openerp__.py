# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': "This is a test module",

    'description': """
        This module is to learn how to create a new module
        and to test if it is recogniced by odoo
    """,

    'author': "Luis González <lgonzalez@vauxoo.com>",
    'website': "http://www.vauxoo.com",

    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'purchase',
        'board',
    ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy_course_view.xml',
        'views/openacademy_session_view.xml',
        'views/openacademy_wizard_view.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'reports/openacademy_session_report.xml',
        'workflows/openacademy_session.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/openacademy_course_demo.xml',
    ],

    'installable': True,
}
