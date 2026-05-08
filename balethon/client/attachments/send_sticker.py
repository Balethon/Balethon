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
            from ...proto import request_pb2, struct_pb2
            peer_id, peer_type = map(int, chat_id.split("|"))
            file_id, access_hash, file_storage_version, sticker_id, collection_id = map(int, sticker.split(":"))
            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="SendMessage",
                payload=request_pb2.SendMessage(
                    peer=struct_pb2.Peer(
                        type=peer_type,
                        id=peer_id
                    ),
                    rid=self.ws_connection.create_rid(),
                    message=struct_pb2.Message(
                        sticker_message=struct_pb2.StickerMessage(
                            sticker_id=struct_pb2.Int32Value(
                                value=sticker_id,
                            ),
                            image512=struct_pb2.ImageLocation(
                                file_location=struct_pb2.FileLocation(
                                    file_id=file_id,
                                    access_hash=access_hash,
                                    file_storage_version=struct_pb2.Int32Value(value=file_storage_version)
                                )
                            ),
                            sticker_collection_id=struct_pb2.Int32Value(
                                value=collection_id
                            )
                        ),
                    ),
                    ex_peer=struct_pb2.Peer(
                        type=peer_type,
                        id=peer_id
                    )
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        sticker = resolve_media(sticker)
        return await self.auto_execute("sendSticker", locals())
