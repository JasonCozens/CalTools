__author__ = 'Jason'

import unittest
import icalendar
import xcal.ijconvert


class IJConvertTest(unittest.TestCase):

    def test_x(self):
        # Arrange.
        expected_result = '["vcalendar"]'
        cal = icalendar.Calendar()
        i_cal = cal.to_ical()
        # Act.
        j_cal = xcal.ijconvert.ICalJCalConverter().convert(i_cal)
        # Assert.
        self.assertEqual(j_cal, expected_result)
