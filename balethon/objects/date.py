from datetime import datetime

from .object import Object


class Date(Object, datetime):

    def __new__(cls, timestamp):
        date_time = datetime.fromtimestamp(timestamp)
        return super().__new__(cls, *date_time.timetuple()[:6])
