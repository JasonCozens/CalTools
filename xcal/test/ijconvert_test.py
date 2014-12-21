__author__ = 'Jason'

import unittest
import icalendar
import icalendar.cal
import icalendar.parser_tools
import icalendar.parser
import icalendar.prop
import xcal.ijconvert
import json
import yaml



class IJConvertTest(unittest.TestCase):

    def test_empty_vcalendar(self):
        # Arrange.
        expected_result = '["vcalendar"]'
        cal = icalendar.Calendar()
        i_cal = cal.to_ical()
        # Act.
        j_cal = xcal.ijconvert.ICalJCalConverter().convert(i_cal)
        # Assert.
        self.assertEqual(j_cal, expected_result)

        icalendar.vCalAddress

    def test_example(self):
        ical_str = """BEGIN:VCALENDAR
CALSCALE:GREGORIAN
PRODID:-//Example Inc.//Example Calendar//EN
VERSION:2.0
BEGIN:VEVENT
DTSTAMP:20080205T191224Z
DTSTART:20081006
SUMMARY:Planning meeting
UID:4088E990AD89CB3DBB484909
END:VEVENT
END:VCALENDAR"""
        cal = icalendar.Calendar()
        cal.add('prodid', '-//Example Inc.//Example Calendar//EN')
        cal.add('version', '2.0')
        c = icalendar.cal.Component()
        c.name = 'VEVENT'
        cal.add_component(c)
        component_name = "vcalendar"
        properties = []
        for skey in cal.singletons:
            properties.append([skey, cal[skey]])
        subcomponents = []
        for sub in cal.subcomponents:
            subcomponents.append(sub)
        jcal = [component_name, properties, subcomponents]

        print(str(jcal))

    def test_json(self):
        self.assertEqual(json.dumps([]), '[]')
        self.assertEqual(json.dumps(['vcalendar']), '["vcalendar"]')
        expected = """[
  "vcalendar",
  [],
  []
]"""
        self.assertEqual(json.dumps(['vcalendar',[],[]],indent=2), expected)
        expected = """[
  "vcalendar",
  [
    [
      "calscale",
      {},
      "text",
      "GREGORIAN"
    ],
    [
      "prodid",
      {},
      "text",
      "-//Example Inc.//Example Calendar//EN"
    ],
    [
      "version",
      {},
      "text",
      "2.0"
    ]
  ],
  [
    [
      "vevent",
      [
        [
          "dtstamp",
          {},
          "date-time",
          "2008-02-05T19:12:24Z"
        ],
        [
          "dtstart",
          {},
          "date",
          "2008-10-06"
        ],
        [
          "summary",
          {},
          "text",
          "Planning meeting"
        ],
        [
          "uid",
          {},
          "text",
          "4088E990AD89CB3DBB484909"
        ]
      ],
      []
    ]
  ]
]"""
        input = ['vcalendar', [
            ['calscale', {}, 'text', 'GREGORIAN'],
            ['prodid', {}, 'text', '-//Example Inc.//Example Calendar//EN'],
            ['version', {}, 'text', '2.0']],
            [['vevent',
                [
                    ['dtstamp', {}, 'date-time', '2008-02-05T19:12:24Z'],
                    ['dtstart', {}, 'date', '2008-10-06'],
                    ['summary', {}, 'text', 'Planning meeting'],
                    ['uid', {}, 'text', '4088E990AD89CB3DBB484909']
                ],
                []
            ]]
        ]
        jcal = json.dumps(input)
        self.assertEqual(json.dumps(input, indent=2), expected)
        print(jcal)
        print(yaml.safe_dump(json.loads(jcal)))

    def test_cal_from_ical(self):
        ical_str = """BEGIN:VCALENDAR
CALSCALE:GREGORIAN
PRODID:-//Example Inc.//Example Calendar//EN
VERSION:2.0
BEGIN:VEVENT
DTSTAMP:20080205T191224Z
DTSTART:20081006
SUMMARY:Planning meeting
UID:4088E990AD89CB3DBB484909
END:VEVENT
END:VCALENDAR"""
        cal = icalendar.Calendar.from_ical(ical_str.encode().replace(b'\n',b'\r\n'))
        for c in cal.walk('VEVENT'):
            print(c.decoded('DTSTART'))