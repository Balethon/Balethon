from typing import Union
from json import dumps

import balethon
from ...objects import Message, ReplyMarkup


class SendContact:

    async def send_contact(
            self: "balethon.Client",
            chat_id: Union[int, str],
            phone_number: str,
            first_name: str,
            last_name: str = None,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            raw_json = {
                "dataType": "contact",
                "data": {
                    "contact": {"name": first_name, "emails": [""], "phones": [phone_number]},
                }
            }
            return await self.execute(requests.SendMessage(
                peer=structs.Peer(
                    type=peer_type,
                    id=peer_id
                ),
                rid=self.ws_connection.create_rid(),
                message=structs.Message(
                    json_message=structs.JsonMessage(
                        raw_json=dumps(raw_json)
                    )
                ),
                ex_peer=structs.Peer(
                    type=peer_type,
                    id=peer_id
                )
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("sendContact", locals())
