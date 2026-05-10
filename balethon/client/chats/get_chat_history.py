from typing import Union, List
from datetime import datetime

import balethon
from ...objects import Message, List as BalethonList
try:
    from balethon.proto import requests, structs, responses
except ImportError:
    pass


class GetChatHistory:

    async def get_chat_history(
            self: "balethon.Client",
            chat_id: Union[int, str],
            date: Union[datetime, int] = -1,
            limit: int = 40
    ) -> List[Message]:
        peer_id, peer_type = map(int, chat_id.split("|"))
        if isinstance(date, datetime):
            date = date.timestamp() * 1000
        peer = structs.Peer(type=peer_type, id=peer_id)
        response = await self.invoke(
            service_name="bale.messaging.v2.Messaging",
            method="LoadHistory",
            payload=requests.LoadHistory(
                peer=peer,
                date=date,
                load_mode=2,
                limit=limit
            )
        )
        history = BalethonList()
        for message_container in response.history:
            fields = [field.name for field in message_container.DESCRIPTOR.fields]
            data = {field: getattr(message_container, field) for field in fields}
            update_message = responses.UpdateMessage(peer=peer, **data)
            message = Message.from_protobuf(update_message)
            history.append(message)
        return history
