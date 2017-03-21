# -*- coding: utf-8 -*-

from openerp.tests.common import TransactionCase
from psycopg2 import IntegrityError
from openerp.tools import mute_logger


class GlobalTestOpenAcademyCourse(TransactionCase):
    """
    Global test to openacademy course model.
    Tests create courses and trigger constraints.
    """

    def setUp(self):
        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.course = self.env['openacademy.course']

    def create_course(self, course_name, course_description,
                      course_responsible_id):
        """ Creates a course with the specified parameters."""
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id,
        })
        return course_id

    @mute_logger('openerp.sql_db')
    def test_10_same_name_description(self):
        """
        This test creates a course using the same value for name and
        description to raise constraint of name different of description.
        """
        with self.assertRaisesRegexp(
                IntegrityError,
                'new row for relation "openacademy_course" violates'
                ' check constraint "openacademy_course_name_description_check"'
                ):
            self.create_course('test', 'test', None)

    @mute_logger('openerp.sql_db')
    def test_20_two_courses_same_name(self):
        """
        This test creates two courses with the same name
        to test unique constraint
        """
        self.create_course("test name", "test description", None)
        with self.assertRaisesRegexp(
                IntegrityError,
                'duplicate key value violates unique constraint '
                '"openacademy_course_name_unique"'
                ):
            self.create_course("test name", "test description2", None)

    def test_30_duplicate_course(self):
        """
        This test creates a course and makes two copies
        to test if it works despite the unique constraint
        """
        new_course = self.create_course("test", "Test description", None)
        new_course.copy()
        new_course.copy()
