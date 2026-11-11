from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media, Message, ReplyMarkup


class SendAudio:

    async def send_audio(
            self: "balethon.Client",
            chat_id: Union[int, str],
            audio: Union[str, bytes, BinaryIO, InputMedia],
            caption: str = None,
            duration: int = None,
            title: str = None,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_chat_id(chat_id)
        audio = resolve_media(audio)

        if self.is_userbot():
            from ...proto import requests, structs, enums
            file = await self.upload_file(chat_id, audio, enums.SEND_TYPE_AUDIO)
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
                            document_ex_audio=structs.DocumentExAudio(
                                duration=duration,
                                track=title or file.name
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

        return await self.auto_execute("sendAudio", locals())
