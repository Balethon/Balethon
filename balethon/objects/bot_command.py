from . import Object


class BotCommand(Object):

    def __init__(
            self,
            command: str,
            description: str,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.command: str = command
        self.description: str = description
