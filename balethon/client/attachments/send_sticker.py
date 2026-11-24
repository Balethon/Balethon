from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media, Message, ReplyMarkup, resolve_message_id


class SendSticker:

    async def send_sticker(
            self: "balethon.Client",
            chat_id: Union[int, str],
            sticker: Union[str, bytes, BinaryIO, InputMedia],
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from ...proto import requests, structs
            reply_to_message_id = resolve_message_id(reply_to_message_id)
            file_id, access_hash, file_storage_version, sticker_id, collection_id = map(int, sticker.split(":"))
            return await self.execute(requests.SendMessage(
                peer=structs.Peer(
                    type=chat_id.peer_type,
                    id=chat_id.peer_id
                ),
                rid=self.ws_connection.create_rid(),
                message=structs.Message(
                    sticker_message=structs.StickerMessage(
                        sticker_id=structs.Int32Value(
                            value=sticker_id,
                        ),
                        image512=structs.ImageLocation(
                            file_location=structs.FileLocation(
                                file_id=file_id,
                                access_hash=access_hash,
                                file_storage_version=structs.Int32Value(value=file_storage_version)
                            )
                        ),
                        sticker_collection_id=structs.Int32Value(
                            value=collection_id
                        )
                    ),
                ),
                ex_peer=structs.Peer(
                    type=chat_id.peer_type,
                    id=chat_id.peer_id
                ),
                **dict(
                    quoted_message_reference=structs.MessageOutReference(
                        peer=structs.OutPeer(type=chat_id.peer_type, id=chat_id.peer_id),
                        rid=reply_to_message_id.rid,
                        date=structs.Int64Value(value=reply_to_message_id.date)
                    ) if reply_to_message_id else None
                )
            ))

        sticker = resolve_media(sticker)
        return await self.auto_execute("sendSticker", locals())
