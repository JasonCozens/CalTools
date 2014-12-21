__author__ = 'Jason'

import icalendar
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
        cal = icalendar.Calendar()
        # Assert.
        self.assertFalse(cal.is_broken)
        self.assertEqual(len(cal.items()), 0)
        self.assertEqual(len(cal.keys()), 0)
        self.assertEqual(cal.subcomponents, [])
        self.assertEqual(len(cal.values()), 0)