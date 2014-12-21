__author__ = 'Jason'

import icalendar
import unittest
from xcal import jcal


class JCalTest(unittest.TestCase):

    def test_new_calendar(self):
        # Arrange.
        cal = icalendar.Calendar()
        # Act.
        j_cal = jcal.JCal.from_calendar(cal)
        # Assert.
        self.assertListEqual(j_cal, ["vcalendar", [], []])

