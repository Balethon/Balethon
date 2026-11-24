from typing import Union
from json import dumps

import balethon
from ...objects import Message, ReplyMarkup, resolve_message_id


class SendLocation:

    async def send_location(
            self: "balethon.Client",
            chat_id: Union[int, str],
            latitude: float,
            longitude: float,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs
            reply_to_message_id = resolve_message_id(reply_to_message_id)
            raw_json = {
                "dataType": "location",
                "data": {
                    "location": {"latitude": latitude, "longitude": longitude}
                }
            }
            return await self.execute(requests.SendMessage(
                peer=structs.Peer(
                    type=chat_id.peer_type,
                    id=chat_id.peer_id
                ),
                rid=self.ws_connection.create_rid(),
                message=structs.Message(
                    json_message=structs.JsonMessage(
                        raw_json=dumps(raw_json)
                    )
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

        return await self.auto_execute("sendLocation", locals())
