from handler import Handler


class CallbackQueryHandler(Handler):

    def __init__(self, callback):
        super().__init__(callback)
