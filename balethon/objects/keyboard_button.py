from . import Object


class KeyboardButton(Object):

    def __init__(
            self,
            text: str = None,
            request_contact: bool = None,
            request_location: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text: str = text
        self.request_contact: bool = request_contact
        self.request_location: bool = request_location
