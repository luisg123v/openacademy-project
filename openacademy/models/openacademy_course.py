# -*- coding: utf-8 -*-

from openerp import models, fields, api

""" This is our first Odoo module"""

class Course(models.Model):
    """
    This class will be used to test
    how models work and how database tables are created
    """

    _name = 'openacademy.course'
    name = fields.Char(string='Title', required=True)
