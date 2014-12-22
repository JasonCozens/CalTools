import icalendar
import icalendar.parser

__author__ = 'Jason'


class ICalJCalConverter():

    def convert(self, i_cal):
        return '["vcalendar"]'


class XCalendar(icalendar.Calendar):

    def __init__(self):
        super().__init__()

    def to_jcal(self):
        self.content_lines()
