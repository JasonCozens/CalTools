__author__ = 'Jason'

import icalendar
import unittest
from cal_tools import jcal
import json


class JCalTest(unittest.TestCase):

    def test_new_calendar(self):
        # Arrange.
        cal = icalendar.Calendar()
        # Act.
        j_cal = jcal.JCal.from_calendar(cal)
        # Assert.
        self.assertListEqual(json.loads(j_cal), ["vcalendar", [], []])

    def test_calendar_with_properties(self):
        # Arrange.
        cal = icalendar.Calendar()
        cal.add('version', '2.0')
        cal.add('prodid', 'test.com/abc')
        # Act.
        j_cal = jcal.JCal.from_calendar(cal)
        # Assert.
        expected = ["vcalendar", [
                    ['version', {}, 'text', '2.0'],
                    ['prodid', {}, 'text', 'test.com/abc']
                ],
                []
        ]
        self.assertListEqual(json.loads(j_cal), expected)
        print(j_cal)

    def test_calendar_with_sub_component(self):
        # Arrange.
        cal = icalendar.Calendar()
        cal.add_component(icalendar.Event())
        # Act.
        j_cal = jcal.JCal.from_calendar(cal)
        # Assert.
        expected = ["vcalendar",
                    [],
                    [["vevent", [], []]]
        ]
        self.assertListEqual(json.loads(j_cal), expected)
        print(j_cal)

    def test_vbool_property(self):
        # Arrange.
        expected = (
            b'BEGIN:VCALENDAR\r\n' +
            b'X-NON-SMOKING:TRUE\r\n' +
            b'END:VCALENDAR\r\n'
        )
        component = icalendar.Calendar.from_ical(expected)
        # component = icalendar.Calendar()
        # component.add('x-non-smoking', True, encode=False)
        # Act.
        prop = jcal.JCal._from_prop(component)
        # Assert.
        self.assertEqual(prop, [['x-non-smoking', {}, 'boolean', True]])
        self.assertEqual(
            json.dumps(prop),
            '[["x-non-smoking", {}, "boolean", true]]')