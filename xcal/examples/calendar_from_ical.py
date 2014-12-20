__author__ = 'Jason'

import icalendar
import unittest


def ical_str_rn(ical_str):
    ical_str = ical_str.replace('\r', '')
    return ical_str.replace('\n', '\r\n')


class NewCalendarExample(unittest.TestCase):

    def test_class_fields(self):
        """

        :return:
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
        self.assertTupleEqual(cal.inclusive, ())
        self.assertFalse(cal.has_key('prodid'))
        self.assertFalse(cal.has_key('version'))
        self.assertFalse(cal.has_key('calscale'))
        self.assertFalse(cal.has_key('method'))



