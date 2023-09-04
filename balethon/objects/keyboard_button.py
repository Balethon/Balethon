from . import Object
import balethon


class KeyboardButton(Object):

    def __init__(
            self,
            client: "balethon.Client" = None,
            text: str = None,
            request_contact: bool = None,
            request_location: bool = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.text: str = text
        self.request_contact: bool = request_contact
        self.request_location: bool = request_location
