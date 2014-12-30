"""Model: A python model of RFC 5545.
=====================================

"""
__author__ = 'Jason'

import datetime
from icalendar import Calendar
from icalendar import Event

ARG_TYPE_INCORRECT = 'Argument should be of type {0}'
REQ_PROP_MISSING = 'Required property {0} is missing'


class CalendarModel():
    """RFC 5545 - Section 3.4. (page 50).::

    Code::

           icalstream = 1*icalobject

           icalobject = "BEGIN" ":" "VCALENDAR" CRLF
                        icalbody
                        "END" ":" "VCALENDAR" CRLF

           icalbody   = calprops component

           calprops   = *(
                      prodid
                      version
                      calscale?
                      method?
                      x-prop*
                      iana-prop*
                      )

           component  = 1*(
                      eventc /
                      todoc /
                      journalc /
                      freebusyc /
                      timezonec /
                      iana-comp /
                      x-comp
                      )

           iana-comp  = "BEGIN" ":" iana-token CRLF
                        1*contentline
                        "END" ":" iana-token CRLF

           x-comp     = "BEGIN" ":" x-name CRLF
                        1*contentline
                        "END" ":" x-name CRLF
    """

    def __init__(self, calendar):
        """

        :param calendar:
        :return: None
        """
        if not isinstance(calendar, Calendar):
            raise AssertionError(ARG_TYPE_INCORRECT.format(Calendar))


class EventModel():

    def __init__(self, event):
        assert isinstance(event, Event),\
            'event is not of type {0}'.format(Event)
        self._uid = None
        self._time_stamp = None
        self._end = None
        self._duration = None
        self._from_event(event)

    def _from_event(self, event):
        assert 'uid' in event.keys(), REQ_PROP_MISSING.format('uid')

    @property
    def uid(self):
        """

        :return:
        """
        assert self._uid is not None

    @property
    def time_stamp(self):
        """dtstamp

        :return:
        """
        assert type(self._time_stamp) is datetime.datetime

    @property
    def start(self):
        """start

        :return: datetime
        """
        pass

    @property
    def event_class(self):
        """

        :return:
        """
        pass

    @property
    def created(self):
        """

        :return:
        """
        pass

    @property
    def description(self):
        """

        :return:
        """
        pass

    @property
    def geo(self):
        """

        :return:
        """
        pass

    @property
    def last_mod(self):
        """

        :return:
        """
        pass

    @property
    def location(self):
        """

        :return:
        """
        pass

    @property
    def organizer(self):
        """

        :return:
        """
        pass

    @property
    def priority(self):
        """

        :return:
        """
        pass

    @property
    def seq(self):
        """

        :return:
        """
        pass

    @property
    def status(self):
        """

        :return:
        """
        pass

    @property
    def summary(self):
        """

        :return:
        """
        pass

    @property
    def transp(self):
        """

        :return:
        """
        pass

    @property
    def url(self):
        """

        :return:
        """
        pass

    @property
    def recur_id(self):
        """

        :return:
        """
        pass

    @property
    def recurrence_rule(self):
        """rrule

        :return: <TODO>
        """
        pass

    @property
    def end(self):
        """dtend

        :return: <TODO>
        """
        assert self._end is None or self._duration is None

    @property
    def duration(self):
        """duration

        :return: <TODO>
        """
        assert self._end is None or self._duration is None

    @property
    def attach(self):
        """rrule

        :return: <TODO>
        """
        return []

    @property
    def attendee(self):
        """rrule

        :return: <TODO>
        """
        return []


    @property
    def categories(self):
        """rrule

        :return: <TODO>
        """
        return []


    @property
    def comment(self):
        """rrule

        :return: <TODO>
        """
        return []

    @property
    def contact(self):
        """rrule

        :return: <TODO>
        """
        return []

    @property
    def exclude_dates(self):
        """rrule

        :return: <TODO>
        """
        return []

    @property
    def rs_status(self):
        """rrule

        :return: <TODO>
        """
        return []

    @property
    def related(self):
        """rrule

        :return: <TODO>
        """
        return []

    @property
    def resources(self):
        """rrule

        :return: <TODO>
        """
        return []

    @property
    def r_date(self):
        """rrule

        :return: <TODO>
        """
        return []

    @property
    def x_prop(self):
        """rrule

        :return: <TODO>
        """
        return []

    @property
    def iana_prop(self):
        """rrule

        :return: <TODO>
        """
        return []