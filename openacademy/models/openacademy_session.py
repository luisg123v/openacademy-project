# -*- coding: utf-8 -*-

from openerp import models, fields, api

""" This is our second Odoo module"""


class Session(models.Model):
    """
    This class will be used to test
    how models work and how database tables are created
    """

    _name = 'openacademy.session'
    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=['|', ('instructor', '=', True),
                     ('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)

    attendee_ids = fields.Many2many('res.partner', string="Attendees")
