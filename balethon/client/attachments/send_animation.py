from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media, Message, ReplyMarkup


class SendAnimation:

    async def send_animation(
            self: "balethon.Client",
            chat_id: Union[int, str],
            animation: Union[str, bytes, BinaryIO, InputMedia],
            duration: int = None,
            width: int = None,
            height: int = None,
            caption: str = None,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        animation = resolve_media(animation)

        if self.is_userbot():
            from ...proto import requests, structs, enums
            peer_id, peer_type = map(int, chat_id.split("|"))
            file = await self.upload_file(chat_id, animation, enums.SEND_TYPE_GIF)
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
                        document_message=structs.DocumentMessage(
                            file_id=file.id,
                            access_hash=peer_id,
                            file_size=file.size,
                            name=file.name,
                            mime_type=file.mime_type,
                            ext=structs.DocumentEx(
                                document_ex_gif=structs.DocumentExGif(
                                    w=100,
                                    h=100,
                                    duration=10
                                )
                            ),
                            caption=structs.TextMessage(text=caption)
                        )
                    ),
                    ex_peer=structs.Peer(
                        type=peer_type,
                        id=peer_id
                    )
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute(
            "sendAnimation",
            locals(),
            json=False,  # The sendAnimation method only works with multipart/form-data
        )
