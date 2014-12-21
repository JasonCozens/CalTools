__author__ = 'Jason'

class JCal():

    @classmethod
    def from_calendar(cls, cal):
        properties = []
        for key in cal.keys():
            properties.append([key.lower(), {}, 'text', cal.decoded(key)])
        return [cal.name.lower(), properties, []]
