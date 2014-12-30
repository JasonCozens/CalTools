__author__ = 'Jason'

import unittest
from icalendar import Calendar
from cal_tools import model
from cal_tools.model import CalendarModel

print_help = True


class CalendarModelTest(unittest.TestCase):

    def test_calendar_type_incorrect(self):
        # Act.
        with self.assertRaises(AssertionError) as ex:
            CalendarModel(None)
        # Info.
        if print_help:
            print(ex.exception.args[0])
        # Assert.
        self.assertEqual(
            ex.exception.args[0],
            model.ARG_TYPE_INCORRECT.format(Calendar))

    def test_required_property_prod_id_is_missing(self):
        # Arrange.
        calendar = Calendar()
        # Act.
        with self.assertRaises(AssertionError) as ex:
            CalendarModel(calendar)
        # Info.
        if print_help:
            print(ex.exception.args[0])
        # Assert.
        self.assertEqual(
            ex.exception.args[0],
            model.REQ_PROP_MISSING.format('PRODID'))

    def test_required_property_version_is_missing(self):
        # Arrange.
        i_cal = (
            b'BEGIN:VCALENDAR\r\n' +
            b'PRODID:test.com/abc\r\n' +
            b'END:VCALENDAR\r\n'
        )
        calendar = Calendar.from_ical(i_cal)
        # Act.
        with self.assertRaises(AssertionError) as ex:
            CalendarModel(calendar)
        # Info.
        if print_help:
            print(ex.exception.args[0])
        # Assert.
        self.assertEqual(
            ex.exception.args[0],
            model.REQ_PROP_MISSING.format('VERSION'))
