from .handler import Handler


class MessageHandler(Handler):

    def __init__(self, callback):
        super().__init__(callback)
