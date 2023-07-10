from .handler import Handler


class CallbackQueryHandler(Handler):

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
