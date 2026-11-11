from typing import Union

import balethon
from ...objects import Message
from balethon import objects


class SendMessage:

    async def send_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            text: str,
            reply_markup: "objects.ReplyMarkup" = None,
            reply_to_message_id: int = None,
            message_thread_id: int = None
    ) -> Message:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs
            return await self.execute(requests.SendMessage(
                peer=structs.Peer(
                    type=chat_id.peer_type,
                    id=chat_id.peer_id
                ),
                rid=self.ws_connection.create_rid(),
                message=structs.Message(
                    text_message=structs.TextMessage(
                        text=text
                    )
                ),
                ex_peer=structs.Peer(
                    type=chat_id.peer_type,
                    id=chat_id.peer_id
                )
            ))

        return await self.auto_execute("sendMessage", locals())
