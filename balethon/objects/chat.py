from . import Object


class Chat(Object):
    id: int
    type: str
    title: str
    username: str
    first_name: str
    last_name: str
    all_members_are_administrators: bool
    description: str
    invite_link: str
    pinned_message: None
    sticker_set_name: str
    can_set_sticker_set: bool
