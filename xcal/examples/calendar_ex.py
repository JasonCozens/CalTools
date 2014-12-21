__author__ = 'Jason'

import icalendar
from icalendar import (
    vText,
)
import unittest


def ical_str_rn(ical_str):
    ical_str = ical_str.replace('\r', '')
    return ical_str.replace('\n', '\r\n')


class NewCalendarExample(unittest.TestCase):

    def test_class_fields(self):
        """Component class fields.

        :return: void
        The main classes in icalendar inherit fom Component which has the
        following class fields:

        * name
        * required
        * singletons
        * multiple
        * exclusive
        * inclusive
        * ignore_exceptions
        """
        # Act.
        cal = icalendar.Calendar()
        # Assert.
        self.assertEqual(cal.name, 'VCALENDAR')
        self.assertTupleEqual(
            cal.canonical_order,
            ('VERSION', 'PRODID', 'CALSCALE', 'METHOD', ))
        self.assertTupleEqual(cal.required, ('prodid', 'version', ))
        self.assertTupleEqual(cal.singletons, ('prodid', 'version', ))
        self.assertTupleEqual(cal.multiple, ('calscale', 'method', ))
        self.assertTupleEqual(cal.exclusive, ())
        self.assertTupleEqual(cal.inclusive, ())
        self.assertFalse(cal.ignore_exceptions)
        self.assertFalse(cal.has_key('prodid'))
        self.assertFalse(cal.has_key('version'))
        self.assertFalse(cal.has_key('calscale'))
        self.assertFalse(cal.has_key('method'))

    def test_instance_fields(self):
        # Act.
        cal = icalendar.Calendar()
        # Assert.
        self.assertFalse(cal.is_broken)
        self.assertEqual(len(cal.items()), 0)
        self.assertEqual(len(cal.keys()), 0)
        self.assertEqual(cal.subcomponents, [])
        self.assertEqual(len(cal.values()), 0)

    def test_add_one_item(self):
        # Arrange.
        cal = icalendar.Calendar()
        # Act.
        cal.add('name', 'value')
        # Assert.
        self.assertEqual(len(cal.items()), 1)
        self.assertEqual(list(cal.items()), [('NAME', vText('value'))])
        self.assertEqual(list(cal.keys()), ['NAME'])
        self.assertEqual(list(cal.values()), [vText('value')])

    def test_new_calendar_to_ical(self):
        """The ical output for an empty Calendar object.

        :return:
        """
        # Arrange.
        cal = icalendar.Calendar()
        # Act.
        ical = cal.to_ical()
        # Assert.
        self.assertEqual(ical, b'BEGIN:VCALENDAR\r\nEND:VCALENDAR\r\n')

    def test_calendar_with_required_properties(self):
        """The ical output for a Calendar object with required properties.

        :return:
        """
        # Arrange.
        cal = icalendar.Calendar()
        # Act.
        cal.add('version', '2.0')
        cal.add('prodid', 'test.com/abc')
        ical = cal.to_ical()
        # Assert.
        expected = (
            b'BEGIN:VCALENDAR\r\n' +
            b'VERSION:2.0\r\n' +
            b'PRODID:test.com/abc\r\n' +
            b'END:VCALENDAR\r\n'
        )
        self.assertEqual(ical, expected)

    def test_calendar_has_key(self):
        # Arrange.
        cal = icalendar.Calendar()
        # Pre-Assert.
        self.assertFalse(cal.has_key('version'))
        # Act.
        cal.add('version', '2.0')
        # Post-Assert.
        self.assertTrue(cal.has_key('version'))

    def test_calendar_decoded(self):
        # Arrange.
        cal = icalendar.Calendar()
        # Act.
        cal.add('version', '2.0')
        # Post-Assert.
        self.assertEqual(cal.decoded('version'), b'2.0')

    def test_calendar_content_lines(self):
        # Arrange.
        cal = icalendar.Calendar()
        # Act.
        cal.add('version', '2.0')
        # Post-Assert.
        self.assertListEqual(
            cal.content_lines(),
            ['BEGIN:VCALENDAR', 'VERSION:2.0', 'END:VCALENDAR', ''])
