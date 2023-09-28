from . import Object


class ReplyMarkup(Object, list):

    @classmethod
    def wrap(cls, raw_object):
        return raw_object

    def __init__(
            self,
            *rows,
            **kwargs
    ):
        super().__init__(**kwargs)
        list.__init__(self, rows)

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(repr(i) for i in self)})"
