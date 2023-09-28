from . import Object
from balethon import objects


class Chat(Object):

    def __init__(
            self,
            id: int = None,
            type: str = None,
            title: str = None,
            username: str = None,
            first_name: str = None,
            last_name: str = None,
            all_members_are_administrators: bool = None,
            description: str = None,
            invite_link: str = None,
            pinned_message: "objects.Message" = None,
            sticker_set_name: str = None,
            can_set_sticker_set: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: int = id
        self.type: str = type
        self.title: str = title
        self.username: str = username
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.all_members_are_administrators: bool = all_members_are_administrators
        self.description: str = description
        self.invite_link: str = invite_link
        self.pinned_message: "objects.Message" = pinned_message
        self.sticker_set_name: str = sticker_set_name
        self.can_set_sticker_set: bool = can_set_sticker_set

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.first_name:
            return self.first_name
        return ""
