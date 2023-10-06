from . import Object


class ReplyMarkup(Object):

    @classmethod
    def wrap(cls, raw_object):
        for subclass in cls.__subclasses__():
            try:
                return subclass.wrap(raw_object)
            except KeyError:
                continue
