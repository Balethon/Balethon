from typing import List

from . import Object
from balethon import objects


class Message(Object):
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
            forward_from: "objects.User" = None,
            forward_from_chat: "objects.Chat" = None,
            forward_from_message_id: int = None,
            forward_date: "objects.Date" = None,
            reply_to_message: "objects.Message" = None,
            edit_date: "objects.Date" = None,
            text: str = None,
            entities: None = None,
            caption_entities: None = None,
            audio: "objects.Audio" = None,
            document: "objects.Document" = None,
            photo: None = None,
            video: "objects.Video" = None,
            voice: "objects.Voice" = None,
            caption: str = None,
            contact: "objects.Contact" = None,
            location: "objects.Location" = None,
            new_chat_members: None = None,  # TODO: adding support for List in Object.validate_types()
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
        super().__init__(**kwargs)
        self.id: int = id
        self.author: "objects.User" = author
        self.date: "objects.Date" = date
        self.chat: "objects.Chat" = chat
        self.forward_from: "objects.User" = forward_from
        self.forward_from_chat: "objects.Chat" = forward_from_chat
        self.forward_from_message_id: int = forward_from_message_id
        self.forward_date: "objects.Date" = forward_date
        self.reply_to_message: "objects.Message" = reply_to_message
        self.edit_date: "objects.Date" = edit_date
        self.text: str = text
        self.entities: List["objects.Entity"] = entities
        self.caption_entities: List["objects.Entity"] = caption_entities
        self.audio: "objects.Audio" = audio
        self.document: "objects.Document" = document
        self.photo: None = photo
        self.video: "objects.Video" = video
        self.voice: "objects.Voice" = voice
        self.caption: str = caption
        self.contact: "objects.Contact" = contact
        self.location: "objects.Location" = location
        self.new_chat_members: List["objects.User"] = new_chat_members
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

    async def reply(self, text, reply_markup=None, client=None):
        client = client or self.client
        return await client.send_message(self.chat.id, text, reply_markup, self.id)

    async def edit_text(self,  text, reply_markup=None, client=None):
        client = client or self.client
        return await client.edit_message_text(self.chat.id, self.id, text, reply_markup)

    async def delete(self, client=None):
        client = client or self.client
        return await client.delete_message(self.chat.id, self.id)
