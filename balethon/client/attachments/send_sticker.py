from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media, Message, ReplyMarkup


class SendSticker:

    async def send_sticker(
            self: "balethon.Client",
            chat_id: Union[int, str],
            sticker: Union[str, bytes, BinaryIO, InputMedia],
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        if self.is_userbot():
            from ...proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            file_id, access_hash, file_storage_version, sticker_id, collection_id = map(int, sticker.split(":"))
            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="SendMessage",
                payload=requests.SendMessage(
                    peer=structs.Peer(
                        type=peer_type,
                        id=peer_id
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
                        type=peer_type,
                        id=peer_id
                    )
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        sticker = resolve_media(sticker)
        return await self.auto_execute("sendSticker", locals())
