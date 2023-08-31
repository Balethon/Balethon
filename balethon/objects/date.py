from datetime import datetime

from .object import Object


class Date(Object, datetime):

    def __new__(cls, timestamp):\
        return datetime.fromtimestamp(timestamp)
