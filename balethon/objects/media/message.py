from .. import Object
from .. import User
from .. import Date
from .. import Chat


class Message(Object):

    def __init__(
            self,
            client=None,
            id: int = None,
            author: User = None,
            date: Date = None,
            chat: Chat = None,
            forward_from: None = None,
            forward_from_chat: Chat = None,
            forward_from_message_id: int = None,
            forward_date: Date = None,
            reply_to_message: None = None,
            edit_date: Date = None,
            text: str = None,
            entities: None = None,
            caption_entities: None = None,
            audio: None = None,
            document: None = None,
            photo: None = None,
            video: None = None,
            voice: None = None,
            caption: None = None,
            contact: None = None,
            location: None = None,
            new_chat_members: None = None,
            left_chat_member: None = None,
            new_chat_title: None = None,
            new_chat_photo: None = None,
            delete_chat_photo: None = None,
            group_chat_created: None = None,
            supergroup_chat_created: None = None,
            channel_chat_created: None = None,
            pinned_message: None = None,
            invoice: None = None,
            successful_payment: None = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.id: int = id
        self.author: User = author
        self.date: Date = date
        self.chat: Chat = chat
        self.forward_from: None = forward_from
        self.forward_from_chat: Chat = forward_from_chat
        self.forward_from_message_id: int = forward_from_message_id
        self.forward_date: Date = forward_date
        self.reply_to_message: None = reply_to_message
        self.edit_date: Date = edit_date
        self.text: str = text
        self.entities: None = entities
        self.caption_entities: None = caption_entities
        self.audio: None = audio
        self.document: None = document
        self.photo: None = photo
        self.video: None = video
        self.voice: None = voice
        self.caption: None = caption
        self.contact: None = contact
        self.location: None = location
        self.new_chat_members: None = new_chat_members
        self.left_chat_member: None = left_chat_member
        self.new_chat_title: None = new_chat_title
        self.new_chat_photo: None = new_chat_photo
        self.delete_chat_photo: None = delete_chat_photo
        self.group_chat_created: None = group_chat_created
        self.supergroup_chat_created: None = supergroup_chat_created
        self.channel_chat_created: None = channel_chat_created
        self.pinned_message: None = pinned_message
        self.invoice: None = invoice
        self.successful_payment: None = successful_payment

    @classmethod
    def wrap(cls, raw_object):
        if raw_object.get("message_id"):
            raw_object["id"] = raw_object.pop("message_id")
        if raw_object.get("from"):
            raw_object["author"] = raw_object.pop("from")
        return super().wrap(raw_object)

    async def reply(self, text, reply_markup=None, client=None):
        client = client or self.client
        return await client.send_message(self.chat.id, text, reply_markup, self.id)

    async def edit_text(self,  text, reply_markup=None, client=None):
        client = client or self.client
        return await client.edit_message_text(self.chat.id, self.id, text, reply_markup)

    async def delete(self, client=None):
        client = client or self.client
        return await client.delete_message(self.chat.id, self.id)
