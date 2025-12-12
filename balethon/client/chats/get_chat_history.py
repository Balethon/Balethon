from typing import Union, List
from datetime import datetime

import balethon
from ...objects import Message, List as BalethonList
from balethon.proto import request_pb2, struct_pb2, response_pb2


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
        peer = struct_pb2.Peer(type=peer_type, id=peer_id)
        response = await self.invoke(
            service_name="bale.messaging.v2.Messaging",
            method="LoadHistory",
            payload=request_pb2.LoadHistory(
                peer=peer,
                date=date,
                load_mode=2,
                limit=limit
            )
        )
        result = response_pb2.LoadHistory()
        result.ParseFromString(response)
        history = BalethonList()
        for message_container in result.history:
            fields = [field.name for field in message_container.DESCRIPTOR.fields]
            data = {field: getattr(message_container, field) for field in fields}
            update_message = response_pb2.UpdateMessage(peer=peer, **data)
            message = Message.from_protobuf(update_message)
            history.append(message)
        return history
