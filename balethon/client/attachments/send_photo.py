from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media, Message, ReplyMarkup


class SendPhoto:

    async def send_photo(
            self: "balethon.Client",
            chat_id: Union[int, str],
            photo: Union[str, bytes, BinaryIO, InputMedia],
            caption: str = None,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_chat_id(chat_id)
        photo = resolve_media(photo)

        if self.is_userbot():
            from ...proto import requests, structs, enums
            file = await self.upload_file(chat_id, photo, enums.SEND_TYPE_PHOTO)
            return await self.execute(requests.SendMessage(
                peer=structs.Peer(
                    type=chat_id.peer_type,
                    id=chat_id.peer_id
                ),
                rid=self.ws_connection.create_rid(),
                message=structs.Message(
                    document_message=structs.DocumentMessage(
                        file_id=file.id,
                        access_hash=chat_id.peer_id,
                        file_size=file.size,
                        name=file.name,
                        mime_type=file.mime_type,
                        ext=structs.DocumentEx(
                            document_ex_photo=structs.DocumentExPhoto(
                                w=100,
                                h=100
                            )
                        ),
                        caption=structs.TextMessage(text=caption)
                    )
                ),
                ex_peer=structs.Peer(
                    type=chat_id.peer_type,
                    id=chat_id.peer_id
                )
            ))

        return await self.auto_execute("sendPhoto", locals())
