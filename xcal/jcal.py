__author__ = 'Jason'

import json


class JCal():

    @classmethod
    def from_calendar(cls, cal):
        properties = []
        for key in cal.keys():
            properties.append(
                [key.lower(),
                    {},
                 'text',
                 cal.decoded(key).decode()])
        components = []
        for sub in cal.subcomponents:
            components.append(["vevent", [], []])
        return json.dumps([cal.name.lower(), properties, components])
