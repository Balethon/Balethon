from ..object import Object
from .. import User
from ..date import Date


class Message(Object):
    id: int
    author: User
    date: Date
    chat: None
    forward_from: User
    forward_from_chat: None
    forward_from_message_id: int
    forward_date: Date
    reply_to_message: None
    edit_date: Date
    text: str
    entities: None
    caption_entities: None
    audio: None
    document: None
    photo: None
    video: None
    voice: None
    caption: None
    contact: None
    location: None
    new_chat_members: None
    left_chat_member: None
    new_chat_title: None
    new_chat_photo: None
    delete_chat_photo: None
    group_chat_created: None
    supergroup_chat_created: None
    channel_chat_created: None
    pinned_message: None
    invoice: None
    successful_payment: None

    def __init__(self, **kwargs):
        if kwargs.get("message_id"):
            kwargs["id"] = kwargs.pop("message_id")
        if kwargs.get("from"):
            kwargs["author"] = kwargs.pop("from")
        super().__init__(**kwargs)
