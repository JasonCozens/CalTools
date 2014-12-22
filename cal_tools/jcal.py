__author__ = 'Jason'

import json


class JCal():

    @classmethod
    def from_calendar(cls, calendar):
        """Convert a Calendar instance to a json string.

        :param calendar: icalendar.Calendar
        :return: json str
        """
        return json.dumps(JCal._from_component(calendar))

    @classmethod
    def _from_component(cls, component):
        """Convert a Component to a list representation.

        :param component: icalendar.Component
        :return: list
        """
        properties = JCal._from_prop(component)
        components = []
        for sub_component in component.subcomponents:
            components.append(JCal._from_component(sub_component))
        return [component.name.lower(), properties, components]

    @classmethod
    def _from_prop(cls, component):
        properties = []
        for key in component.keys():
            properties.append(
                [key.lower(),
                    {},
                 'text',
                 component.decoded(key).decode()])
        return properties