__author__ = 'Jason'

class JCal():

    @classmethod
    def from_calendar(cls, cal):
        return [cal.name.lower(), [], []]
