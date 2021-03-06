# -*- coding: utf-8 -*-

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError
from psycopg2 import IntegrityError
from openerp.tools import mute_logger


class GlobalTestOpenAcademySession(TransactionCase):
    """
    Global test to openacademy session model.
    Tests create sessions and trigger constraints.
    """

    def setUp(self):
        super(GlobalTestOpenAcademySession, self).setUp()
        # Define global variables to test methods
        self.session = self.env['openacademy.session']
        self.partner_vauxoo = self.env.ref('base.res_partner_23')
        self.course = self.env.ref('openacademy.course1')
        self.partner_attendee = self.env.ref('base.res_partner_5')

    def test_10_instructor_is_attendee(self):
        """
        This test creates a partner and asigns it as an instructor
        and as an atendee to check Python constraint
        """
        with self.assertRaisesRegexp(
                ValidationError,
                "A session's instructor can't be an attendee"
                ):
            self.session.create({
                'name': 'test 1',
                'seats': 1,
                'instructor_id': self.partner_vauxoo.id,
                'attendee_ids': [(6, 0, [self.partner_vauxoo.id])],
                'course_id': self.course.id, })

    def test_20_wkf_done(self):
        """
        This test follows every workflow state to test
        if they work correctly
        """
        session_test = self.session.create({
            'name': 'Session test 1',
            'seats': 2,
            'instructor_id': self.partner_vauxoo.id,
            'attendee_ids': [(6, 0, [self.partner_attendee.id])],
            'course_id': self.course.id, })
        # Check initial state
        self.assertEqual(session_test.state,
                         'draft',
                         'Initial state should be in "draft"')

        # Change next state and check it
        session_test.signal_workflow('button_confirm')
        self.assertEqual(session_test.state,
                         'confirmed', "Signal confirm doesn't work fine!")

        # Change next state and check it
        session_test.signal_workflow('button_done')
        self.assertEqual(session_test.state,
                         'done', "Signal done doesn't work fine!")

    @mute_logger('openerp.sql_db')
    def test_30_without_course(self):
        with self.assertRaisesRegexp(
                IntegrityError,
                'null value in column "course_id"'
                ' violates not-null constraint'):
            self.session.create({
                'name': 'test 1', })
