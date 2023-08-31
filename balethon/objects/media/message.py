from ..object import Object
from ..user import User
from ..date import Date
from ..chat import Chat


class Message(Object):
    id: int
    author: User
    date: Date
    chat: Chat
    forward_from: None
    forward_from_chat: Chat
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

    async def reply(self, text, reply_markup=None, client=None):
        client = client or self.client
        return await client.send_message(self.chat.id, text, reply_markup, self.id)

    async def edit_text(self,  text, reply_markup=None, client=None):
        client = client or self.client
        return await client.edit_message_text(self.chat.id, self.id, text, reply_markup)
