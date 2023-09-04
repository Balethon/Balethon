from . import Object
import balethon
from balethon import objects


class Message(Object):

    def __init__(
            self,
            client: "balethon.Client" = None,
            id: int = None,
            author: "objects.User" = None,
            date: "objects.Date" = None,
            chat: "objects.Chat" = None,
            forward_from: "objects.User" = None,
            forward_from_chat: "objects.Chat" = None,
            forward_from_message_id: int = None,
            forward_date: "objects.Date" = None,
            reply_to_message: "objects.Message" = None,
            edit_date: "objects.Date" = None,
            text: str = None,
            entities: None = None,
            caption_entities: None = None,
            audio: None = None,
            document: None = None,
            photo: None = None,
            video: None = None,
            voice: None = None,
            caption: str = None,
            contact: None = None,
            location: None = None,
            new_chat_members: list["objects.User"] = None,
            left_chat_member: "objects.User" = None,
            new_chat_title: str = None,
            new_chat_photo: None = None,
            delete_chat_photo: bool = None,
            group_chat_created: bool = None,
            supergroup_chat_created: bool = None,
            channel_chat_created: bool = None,
            pinned_message: None = None,
            invoice: None = None,
            successful_payment: None = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.id: int = id
        self.author: "objects.User" = author
        self.date: "objects.Date" = date
        self.chat: "objects.Chat" = chat
        self.forward_from: None = forward_from
        self.forward_from_chat: "objects.Chat" = forward_from_chat
        self.forward_from_message_id: int = forward_from_message_id
        self.forward_date: "objects.Date" = forward_date
        self.reply_to_message: "objects.Message" = reply_to_message
        self.edit_date: "objects.Date" = edit_date
        self.text: str = text
        self.entities: None = entities
        self.caption_entities: None = caption_entities
        self.audio: None = audio
        self.document: None = document
        self.photo: None = photo
        self.video: None = video
        self.voice: None = voice
        self.caption: str = caption
        self.contact: None = contact
        self.location: None = location
        self.new_chat_members: list["objects.User"] = new_chat_members
        self.left_chat_member: "objects.User" = left_chat_member
        self.new_chat_title: str = new_chat_title
        self.new_chat_photo: None = new_chat_photo
        self.delete_chat_photo: bool = delete_chat_photo
        self.group_chat_created: bool = group_chat_created
        self.supergroup_chat_created: bool = supergroup_chat_created
        self.channel_chat_created: bool = channel_chat_created
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
