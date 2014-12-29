__author__ = 'Jason'

import unittest
import icalendar
from icalendar import (
    vText,
)


class Examples5545(unittest.TestCase):
    """Examples from RFC 5545. (http://tools.ietf.org/html/rfc5545)

    .
    """
    def test_3_4(self):
        # Arrange.
        ical_str = (
            'BEGIN:VCALENDAR\r\n'
            'VERSION:2.0\r\n'
            'PRODID:-//hacksw/handcal//NONSGML v1.0//EN\r\n'
            'BEGIN:VEVENT\r\n'
            'UID:19970610T172345Z-AF23B2@example.com\r\n'
            'DTSTAMP:19970610T172345Z\r\n'
            'DTSTART:19970714T170000Z\r\n'
            'DTEND:19970715T040000Z\r\n'
            'SUMMARY:Bastille Day Party\r\n'
            'END:VEVENT\r\n'
            'END:VCALENDAR\r\n'
        )
        # Act.
        cal = icalendar.Calendar.from_ical(ical_str)
        sub_components = cal.subcomponents
        # Assert.
        # 1. type.
        self.assertEqual(cal.name, 'VCALENDAR')
        # 2. properties.
        self.assertEqual(len(cal.items()), 2)
        self.assertIn('version', cal.keys())
        self.assertIn('prodid', cal.keys())
        self.assertEqual(cal['version'], vText('2.0'))
        self.assertEqual(
            cal['prodid'],
            vText('-//hacksw/handcal//NONSGML v1.0//EN'))
        self.assertEqual(cal.decoded('version'), b'2.0')
        self.assertEqual(
            cal.decoded('prodid'),
            b'-//hacksw/handcal//NONSGML v1.0//EN')
        # Subcomponents.
        self.assertEqual(1, len(sub_components))
        v_event = sub_components[0]
        self.assertEqual(len(v_event.items()), 5)
        self.assertEqual(len(v_event.subcomponents), 0)

    def test_3_6_1_opaque_event(self):
        # Arrange.
        self.ical_str = (
            'BEGIN:VEVENT\r\n'
            'UID:19970901T130000Z-123401@example.com\r\n'
            'DTSTAMP:19970901T130000Z\r\n'
            'DTSTART:19970903T163000Z\r\n'
            'DTEND:19970903T190000Z\r\n'
            'SUMMARY:Annual Employee Review\r\n'
            'CLASS:PRIVATE\r\n'
            'CATEGORIES:BUSINESS,HUMAN RESOURCES\r\n'
            'END:VEVENT\r\n'
        )
        # Act.
        cal = icalendar.Calendar.from_ical(self.ical_str)
        # Assert.
        self.assertEqual(cal.name, 'VEVENT')
        self.assertEqual(len(cal.items()), 7)
        self.assertEqual(len(cal.subcomponents), 0)

    def test_3_6_1_transparent_event(self):
        # Arrange.
        self.ical_str = (
            'BEGIN:VEVENT\r\n'
            'UID:19970901T130000Z-123402@example.com\r\n'
            'DTSTAMP:19970901T130000Z\r\n'
            'DTSTART:19970401T163000Z\r\n'
            'DTEND:19970402T010000Z\r\n'
            'SUMMARY:Laurel is in sensitivity awareness class.\r\n'
            'CLASS:PUBLIC\r\n'
            'CATEGORIES:BUSINESS,HUMAN RESOURCES\r\n'
            'TRANSP:TRANSPARENT\r\n'
            'END:VEVENT\r\n'
        )
        # Act.
        cal = icalendar.Calendar.from_ical(self.ical_str)
        # Assert.
        self.assertEqual(cal.name, 'VEVENT')
        self.assertEqual(len(cal.items()), 8)
        self.assertEqual(len(cal.subcomponents), 0)
