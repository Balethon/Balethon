from balethon.objects import Object


class CopyTextButton(Object):
    def __init__(
            self,
            text: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text: str = text
