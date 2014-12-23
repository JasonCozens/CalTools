__author__ = 'Jason'

import time
import unittest



class JCalTest(unittest.TestCase):

    def test_from_jcal(self):
        """Example of parsing jcal dates and times.

        :return: None
        This examples shows the format strings to use to parse a date or time
        from a jcal json stream.
        """
        # Date only.
        j_cal_date = '2008-02-05'
        date_ex = time.strptime(j_cal_date, '%Y-%m-%d')
        self.assertEqual(date_ex.tm_year, 2008)
        self.assertEqual(date_ex.tm_mon, 2)
        self.assertEqual(date_ex.tm_mday, 5)
        # Time only.
        j_cal_time = '19:12:24Z'
        time_ex = time.strptime(j_cal_time, '%H:%M:%SZ')
        self.assertEqual(time_ex.tm_hour, 19)
        self.assertEqual(time_ex.tm_min, 12)
        self.assertEqual(time_ex.tm_sec, 24)
        # Date and Time.
        j_cal_date_time = '2008-02-05T19:12:24Z'
        date_time_ex = time.strptime(j_cal_date_time, '%Y-%m-%dT%H:%M:%SZ')
        self.assertEqual(date_time_ex.tm_year, 2008)
        self.assertEqual(date_time_ex.tm_mon, 2)
        self.assertEqual(date_time_ex.tm_mday, 5)
        self.assertEqual(date_time_ex.tm_hour, 19)
        self.assertEqual(date_time_ex.tm_min, 12)
        self.assertEqual(date_time_ex.tm_sec, 24)