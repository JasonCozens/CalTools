"""A python model of FRC 5545.

"""
__author__ = 'Jason'


class EventModel():

    def __init__(self):
        self._end = None
        self._duration = None

    @property
    def uid(self):
        pass

    @property
    def time_stamp(self):
        """dtstamp

        :return:
        """
        pass

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