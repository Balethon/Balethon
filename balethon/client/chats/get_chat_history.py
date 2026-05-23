from typing import Union, List
from datetime import datetime

import balethon
from ...objects import Message, List as BalethonList
try:
    from balethon.proto import requests, structs, updates
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
        response = await self.execute(requests.LoadHistory(
            peer=peer,
            date=date,
            load_mode=2,
            limit=limit
        ))
        history = BalethonList()
        for message_container in response.history:
            message_container_fields = [field.name for field in message_container.DESCRIPTOR.fields]
            message_fields = [field.name for field in updates.Message.DESCRIPTOR.fields]
            fields = [field for field in message_container_fields if field in message_fields]
            data = {field: getattr(message_container, field) for field in fields}
            update_message = updates.Message(peer=peer, **data)
            message = Message.from_protobuf(update_message)
            history.append(message)
        return history
