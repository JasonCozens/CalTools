__author__ = 'Jason'

import unittest
from icalendar import Calendar
from cal_tools import model
from cal_tools.model import CalendarModel


class CalendarModelTest(unittest.TestCase):

    def test_calendar_arg_is_correct_type(self):
        # Act.
        with self.assertRaises(AssertionError) as ex:
            CalendarModel(None)
        # Info.
        if __debug__:
            print(ex.exception.args[0])
        # Assert.
        self.assertEqual(
            ex.exception.args[0],
            model.ARG_TYPE_INCORRECT.format(Calendar))

