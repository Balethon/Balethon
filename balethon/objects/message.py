from typing import List, Union, BinaryIO

from . import Object
from balethon import objects
from ..enums import MessageMediaType
from ..sync_support import add_sync_support_to_object


@add_sync_support_to_object
class Message(Object):
    attribute_names = [
        ("id", "message_id"),
        ("author", "from")
    ]

    @classmethod
    def wrap(cls, raw_object):
        try:
            if not raw_object.get("voice") and raw_object["document"]["mime_type"].startswith("audio"):
                raw_object["audio"] = raw_object["document"]
        except (TypeError, KeyError):
            pass
        try:
            if not raw_object.get("video") and raw_object["document"]["mime_type"].startswith("video"):
                raw_object["animation"] = raw_object["document"]
        except (TypeError, KeyError):
            pass
        return super().wrap(raw_object)

    @classmethod
    def from_protobuf(cls, protobuf_data):
        return cls(
            id=f"{protobuf_data.rid}|{protobuf_data.date}",
            author=objects.User(id=protobuf_data.sender_uid),
            chat=objects.Chat(id=f"{protobuf_data.peer.id}|{protobuf_data.peer.type}"),
            date=objects.Date.wrap(protobuf_data.date / 1000),
            text=protobuf_data.message.text_message.text,
            document=objects.Document(
                id=protobuf_data.message.document_message.file_id,
                name=protobuf_data.message.document_message.name,
                size=protobuf_data.message.document_message.file_size,
                mime_type=protobuf_data.message.document_message.mime_type
            ),
            caption=protobuf_data.message.document_message.caption.text
        )

    def __init__(
            self,
            id: int = None,
            author: "objects.User" = None,
            date: "objects.Date" = None,
            chat: "objects.Chat" = None,
            sender_chat: "objects.Chat" = None,
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
            voice: "objects.Voice" = None,
            audio: "objects.Audio" = None,
            document: "objects.Document" = None,
            photo: List["objects.Photo"] = None,
            video: "objects.Video" = None,
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
            web_app_data: "objects.WebAppData" = None,
            reply_markup: "objects.ReplyMarkup" = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: int = id
        self.author: "objects.User" = author
        self.date: "objects.Date" = date
        self.chat: "objects.Chat" = chat
        self.sender_chat: "objects.Chat" = sender_chat
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
        self.voice: "objects.Voice" = voice
        self.audio: "objects.Audio" = audio
        self.document: "objects.Document" = document
        self.photo: List["objects.Photo"] = photo
        self.video: "objects.Video" = video
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
        self.web_app_data: "objects.WebAppData" = web_app_data
        self.reply_markup: "objects.ReplyMarkup" = reply_markup

    @property
    def media_type(self):
        for media_type in MessageMediaType:
            if getattr(self, media_type.value):
                return media_type

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
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.send_animation(
            self.chat.id,
            animation,
            duration,
            width,
            height,
            caption,
            reply_markup,
            self.id
        )

    async def reply_audio(
            self,
            audio: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: str = None,
            duration: int = None,
            title: str = None,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.send_audio(self.chat.id, audio, caption, duration, title, reply_markup, self.id)

    async def reply_contact(
            self,
            phone_number: str,
            first_name: str,
            last_name: str = None,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.send_contact(self.chat.id, phone_number, first_name, last_name, reply_markup, self.id)

    async def reply_document(
            self,
            document: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: str = None,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.send_document(self.chat.id, document, caption, reply_markup, self.id)

    async def reply_location(
            self,
            latitude: int,
            longitude: int,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.send_location(self.chat.id, longitude, latitude, reply_markup, self.id)

    async def reply_media_group(
            self,
            media: List["objects.InputMedia"]
    ):
        return await self.client.send_media_group(self.chat.id, media)

    async def reply_photo(
            self,
            photo: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: str = None,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.send_photo(self.chat.id, photo, caption, reply_markup, self.id)

    async def reply_sticker(
            self,
            sticker: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.send_sticker(self.chat.id, sticker, reply_markup, self.id)

    async def reply_video(
            self,
            video: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            duration: int = None,
            width: int = None,
            height: int = None,
            caption: str = None,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.send_video(self.chat.id, video, duration, width, height, caption, reply_markup)

    async def reply_voice(
            self,
            voice: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: str = None,
            duration: int = None,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.send_voice(self.chat.id, voice, caption, duration, reply_markup, self.id)

    async def reply(
            self,
            text: str,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.send_message(self.chat.id, text, reply_markup, self.id)

    async def edit_text(
            self,
            text: str,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.edit_message_text(self.chat.id, self.id, text, reply_markup)

    async def edit_caption(
            self,
            caption: str,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        return await self.client.edit_message_caption(self.chat.id, self.id, caption, reply_markup)

    async def edit(
            self,
            text: str,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        if self.text:
            return await self.edit_text(text, reply_markup)
        return await self.edit_caption(text, reply_markup)

    async def edit_reply_markup(
            self,
            reply_markup: "objects.ReplyMarkup"
    ):
        return await self.client.edit_message_reply_markup(self.chat.id, self.id, reply_markup)

    async def delete(
            self
    ):
        return await self.client.delete_message(self.chat.id, self.id)

    async def forward(
            self,
            chat_id: Union[int, str]
    ):
        return await self.client.forward_message(chat_id, self.chat.id, self.id)

    async def copy(
            self,
            chat_id: Union[int, str]
    ):
        return await self.client.copy_message(chat_id, self.chat.id, self.id)

    async def send(
            self,
            chat_id: Union[int, str],
            reply_markup: "objects.ReplyMarkup" = None,
            reply_to_message_id: int = None
    ):
        if self.text:
            return await self.client.send_message(
                chat_id,
                self.text,
                reply_markup,
                reply_to_message_id
            )
        elif self.photo:
            return await self.client.send_photo(
                chat_id,
                self.photo[0].id,
                self.caption,
                reply_markup,
                reply_to_message_id
            )
        elif self.voice:
            return await self.client.send_voice(
                chat_id,
                self.voice.id,
                caption=self.caption,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        elif self.audio:
            return await self.client.send_audio(
                chat_id,
                self.audio.id,
                caption=self.caption,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        elif self.video:
            return await self.client.send_video(
                chat_id,
                self.video.id,
                caption=self.caption,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        elif self.animation:
            return await self.client.send_animation(
                chat_id,
                self.animation.id,
                caption=self.caption,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        elif self.contact:
            return await self.client.send_contact(
                chat_id,
                self.contact.phone_number,
                self.contact.first_name,
                self.contact.last_name,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        elif self.location:
            return await self.client.send_location(
                chat_id,
                self.location.longitude,
                self.location.latitude,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        elif self.sticker:
            return await self.client.send_sticker(
                chat_id,
                self.sticker.id,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        elif self.document:
            return await self.client.send_document(
                chat_id,
                self.document.id,
                self.caption,
                reply_markup,
                reply_to_message_id
            )
        raise TypeError("Message is not copyable")
