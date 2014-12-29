"""3.3. Property Value Data Types

    contentline = name *(";" param ) ":" value CRLF
.
"""
__author__ = 'Jason'

import unittest
import icalendar


class VText(unittest.TestCase):

    def test_ical_to_calendar(self):
        # Arrange.
        i_cal_str = 'NOTE;VALUE=TEXT:This is a note.\r\n'
        # Act.
        v_property = icalendar.vText.from_ical(i_cal_str)
        pass


    def test_str_to_v_text(self):
        # Arrange.
        s = 'Hello, world'
        # Act.
        v_text = icalendar.vText(s)
        # Assert.
        self.assertEqual(type(v_text), icalendar.prop.vText)
        self.assertEqual(v_text.to_ical(), b'Hello\\, world')
