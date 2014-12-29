__author__ = 'Jason'

import os
import icalendar


class Examples5545():
    """Examples from RFC 5545. (http://tools.ietf.org/html/rfc5545)

    .
    """
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

    @classmethod
    def example_3_4(cls):
        """

        :return:
        >>> cal = icalendar.Calendar.from_ical(Examples5545.ical_str)
        >>> cal.name
        'VCALENDAR'
        >>> len(cal.subcomponents)
        1

        """
        dt_format = "%d/%m/%y %H:%M"
        print('\nRFC 5545 - Example 3.4.\n', sep='')
        cal = icalendar.Calendar.from_ical(Examples5545.ical_str)
        for component in cal.walk():
            if component.name == "VEVENT":
                print('Event: {0}'.format(component.get('summary')))
                print('Start: {0:{1}}'.
                      format(component.get('dtstart').dt, dt_format))
                print('End: {0:{1}}'.
                      format(component.get('dtend').dt, dt_format))
                print('Time stamp: {0:{1}}'.
                        format(component.get('dtstamp').dt, dt_format))

if __name__ == "__main__":
    Examples5545.example_3_4()