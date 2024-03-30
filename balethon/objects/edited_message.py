from . import Object
from balethon import objects


class EditedMessage(Object):
    attribute_names = [
        ("id", "message_id"),
        ("author", "from")
    ]

    def __init__(
            self,
            id: int = None,
            author: "objects.User" = None,
            date: "objects.Date" = None,
            chat: "objects.Chat" = None,
            edit_date: "objects.Date" = None,
            text: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: int = id
        self.author: "objects.User" = author
        self.date: "objects.Date" = date
        self.chat: "objects.Chat" = chat
        self.edit_date: "objects.Date" = edit_date
        self.text: str = text
