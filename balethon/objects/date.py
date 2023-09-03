from datetime import datetime

from . import Object
import balethon


class Date(Object, datetime):

    @classmethod
    def wrap(cls, raw_object):
        date_time = datetime.fromtimestamp(raw_object)
        return super().__new__(cls, *date_time.timetuple()[:6])

    def __new__(
            cls,
            client: "balethon.Client" = None,
            *args,
            **kwargs
    ):
        return super().__new__(cls, *args, *kwargs)

    def __init__(
            self,
            client: "balethon.Client" = None,
            *args,
            **kwargs
    ):
        super().__init__(client, **kwargs)

    def __repr__(self):
        return str(self)
