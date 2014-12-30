__author__ = 'Jason'

import unittest
from icalendar import Event
from cal_tools import model
from cal_tools.model import EventModel


class EventModelTests(unittest.TestCase):

    def test_event_is_instance_of_event_class(self):
        # Act.
        with self.assertRaises(AssertionError) as ex:
            EventModel(None)

    def test_event(self):
        # Arrange.
        ical_str = (
            'BEGIN:VEVENT\r\n'
            'END:VEVENT\r\n'
        )
        event = Event.from_ical(ical_str)
        # Act.
        with self.assertRaises(AssertionError) as ex:
            event_model = EventModel(event)
        # Assert.
        self.assertEqual(
            ex.exception.args[0],
            model.REQ_PROP_MISSING.format('uid'))

    def test_minimal_event(self):
        ical_str = (
            'BEGIN:VEVENT\r\n'
            'UID:19970610T172345Z-AF23B2@example.com\r\n'
            'DTSTAMP:19970610T172345Z\r\n'
            'END:VEVENT\r\n'
        )
        event_model = EventModel(ical_str)
