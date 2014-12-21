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

    def test_calendar_with_properties(self):
        # Arrange.
        cal = icalendar.Calendar()
        cal.add('version', '2.0')
        cal.add('prodid', 'test.com/abc')
        # Act.
        j_cal = jcal.JCal.from_calendar(cal)
        # Assert.
        expected = ["vcalendar", [
                    ['version', {}, 'text', b'2.0'],
                    ['prodid', {}, 'text', b'test.com/abc']
                ],
                []
        ]
        self.assertListEqual(j_cal, expected)
        print(j_cal)