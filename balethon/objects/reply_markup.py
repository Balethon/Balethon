from . import Object


class ReplyMarkup(Object):

    @classmethod
    def wrap(cls, raw_object):
        from . import InlineKeyboard, ReplyKeyboard
        if "inline_keyboard" in raw_object:
            return InlineKeyboard.wrap(raw_object)
        elif "keyboard" in raw_object:
            return ReplyKeyboard.wrap(raw_object)
