from . import ReplyKeyboard


class ReplyKeyboardRemove(ReplyKeyboard):

    def __init__(self):
        super().__init__(remove=True)

    def __repr__(self):
        return f"{type(self).__name__}()"
