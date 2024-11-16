from typing import List, Union, BinaryIO

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
            animation: "objects.Animation" = None,
            entities: List["objects.Entity"] = None,
            caption_entities: List["objects.Entity"] = None,
            audio: "objects.Audio" = None,
            document: "objects.Document" = None,
            photo: List["objects.Photo"] = None,
            video: "objects.Video" = None,
            voice: "objects.Voice" = None,
            sticker: "objects.Sticker" = None,
            caption: str = None,
            contact: "objects.Contact" = None,
            location: "objects.Location" = None,
            new_chat_members: List["objects.User"] = None,
            left_chat_member: "objects.User" = None,
            new_chat_title: str = None,
            new_chat_photo: List["objects.Photo"] = None,
            delete_chat_photo: bool = None,
            group_chat_created: bool = None,
            supergroup_chat_created: bool = None,
            channel_chat_created: bool = None,
            pinned_message: None = None,
            invoice: "objects.Invoice" = None,
            successful_payment: "objects.SuccessfulPayment" = None,
            media_group_id: int = None,
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
        self.animation: "objects.Animation" = animation
        self.entities: List["objects.Entity"] = entities
        self.caption_entities: List["objects.Entity"] = caption_entities
        self.audio: "objects.Audio" = audio
        self.document: "objects.Document" = document
        self.photo: List["objects.Photo"] = photo
        self.video: "objects.Video" = video
        self.voice: "objects.Voice" = voice
        self.sticker: "objects.Sticker" = sticker
        self.caption: str = caption
        self.contact: "objects.Contact" = contact
        self.location: "objects.Location" = location
        self.new_chat_members: List["objects.User"] = new_chat_members
        self.left_chat_member: "objects.User" = left_chat_member
        self.new_chat_title: str = new_chat_title
        self.new_chat_photo: List["objects.Photo"] = new_chat_photo
        self.delete_chat_photo: bool = delete_chat_photo
        self.group_chat_created: bool = group_chat_created
        self.supergroup_chat_created: bool = supergroup_chat_created
        self.channel_chat_created: bool = channel_chat_created
        self.pinned_message: None = pinned_message
        self.invoice: "objects.Invoice" = invoice
        self.successful_payment: "objects.SuccessfulPayment" = successful_payment
        self.media_group_id: int = media_group_id

    @property
    def content(self) -> str:
        return self.text or self.caption or ""

    @content.setter
    def content(self, value):
        if self.caption or self.document or self.contact or self.location or self.photo:
            self.caption = value
        else:
            self.text = value

    async def reply_animation(
            self,
            animation: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            duration: int = None,
            width: int = None,
            height: int = None,
            caption: str = None,
            client=None
    ):
        client = client or self.client
        return await client.send_animation(self.chat.id, animation, duration, width, height, caption, self.id)

    async def reply_audio(
            self,
            audio: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: str = None,
            duration: int = None,
            title: str = None,
            client=None
    ):
        client = client or self.client
        return await client.send_audio(self.chat.id, audio, caption, duration, title, self.id)

    async def reply_contact(
            self,
            phone_number: str,
            first_name: str,
            last_name: str = None,
            client=None
    ):
        client = client or self.client
        return await client.send_contact(self.chat.id, phone_number, first_name, last_name, self.id)

    async def reply_document(
            self,
            document: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: str = None,
            reply_markup: "objects.ReplyMarkup" = None,
            client=None
    ):
        client = client or self.client
        return await client.send_document(self.chat.id, document, caption, reply_markup, self.id)

    async def reply_location(
            self,
            latitude: int,
            longitude: int,
            client=None
    ):
        client = client or self.client
        return await client.send_location(self.chat.id, longitude, latitude, self.id)

    async def reply_media_group(
            self,
            media: List["objects.InputMedia"],
            client=None
    ):
        client = client or self.client
        return await client.send_media_group(self.chat.id, media)

    async def reply_photo(
            self,
            photo: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: str = None,
            reply_markup: "objects.ReplyMarkup" = None,
            client=None
    ):
        client = client or self.client
        return await client.send_photo(self.chat.id, photo, caption, reply_markup, self.id)

    async def reply_sticker(
            self,
            sticker: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            reply_markup: "objects.ReplyMarkup" = None,
            client=None
    ):
        client = client or self.client
        return await client.send_sticker(self.chat.id, sticker, reply_markup, self.id)

    async def reply_video(
            self,
            video: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            duration: int = None,
            width: int = None,
            height: int = None,
            caption: str = None,
            client=None
    ):
        client = client or self.client
        return await client.send_video(self.chat.id, video, duration, width, height, caption)

    async def reply_voice(
            self,
            voice: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: str = None,
            duration: int = None,
            client=None
    ):
        client = client or self.client
        return await client.send_voice(self.chat.id, voice, caption, duration, self.id)

    async def reply(
            self,
            text: str,
            reply_markup: "objects.ReplyMarkup" = None,
            client=None
    ):
        client = client or self.client
        return await client.send_message(self.chat.id, text, reply_markup, self.id)

    async def edit_text(
            self,
            text,
            reply_markup=None,
            client=None
    ):
        client = client or self.client
        return await client.edit_message_text(self.chat.id, self.id, text, reply_markup)

    async def edit_caption(
            self,
            caption,
            reply_markup=None,
            client=None
    ):
        client = client or self.client
        return await client.edit_message_caption(self.chat.id, self.id, caption, reply_markup)

    async def edit_reply_markup(
            self,
            reply_markup=None,
            client=None
    ):
        if self.text:
            return self.edit_text(self.text, reply_markup, client)
        return await self.edit_caption(self.caption, reply_markup, client)

    async def delete(
            self,
            client=None
    ):
        client = client or self.client
        return await client.delete_message(self.chat.id, self.id)

    async def forward(
            self,
            chat_id,
            client=None
    ):
        client = client or self.client
        return await client.forward_message(chat_id, self.chat.id, self.id)

    async def copy(
            self,
            chat_id,
            client=None
    ):
        client = client or self.client
        return await client.copy_message(chat_id, self.chat.id, self.id)

    async def send(
            self,
            chat_id,
            reply_markup: "objects.ReplyMarkup" = None,
            reply_to_message_id=None,
            client=None
    ):
        client = client or self.client
        if self.text:
            return await client.send_message(
                chat_id,
                self.text,
                reply_markup,
                reply_to_message_id
            )
        elif self.photo:
            return await client.send_photo(
                chat_id,
                self.photo[0].id
            )
        elif self.audio:
            return await client.send_audio(
                chat_id,
                self.audio.id,
                caption=self.caption,
                reply_to_message_id=reply_to_message_id
            )
        elif self.video:
            return await client.send_video(
                chat_id,
                self.video.id,
                caption=self.caption,
                reply_to_message_id=reply_to_message_id
            )
        elif self.animation:
            return await client.send_animation(
                chat_id,
                self.animation.id,
                caption=self.caption,
                reply_to_message_id=reply_to_message_id
            )
        elif self.contact:
            return await client.send_contact(
                chat_id,
                self.contact.phone_number,
                self.contact.first_name,
                self.contact.last_name,
                reply_to_message_id=reply_to_message_id
            )
        elif self.location:
            return await client.send_location(
                chat_id,
                self.location.longitude,
                self.location.latitude,
                reply_to_message_id=reply_to_message_id
            )
        elif self.voice:
            return await client.send_voice(
                chat_id,
                self.voice.id,
                caption=self.caption,
                reply_to_message_id=reply_to_message_id
            )
        elif self.sticker:
            return await client.send_sticker(
                chat_id,
                self.sticker.id,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        elif self.document:
            return await client.send_document(
                chat_id,
                self.document.id,
                self.caption,
                reply_markup,
                reply_to_message_id
            )
        raise TypeError("Message is not copyable")
