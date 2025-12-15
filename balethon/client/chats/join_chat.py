from re import search
from typing import Union

import balethon
from ...proto.response_pb2 import JoinGroup, JoinPublicGroup
from balethon.proto import request_pb2, struct_pb2


class JoinChat:
    
    async def join_chat(
            self: "balethon.Client",
            chat_id: str
    ) -> Union[JoinGroup, JoinPublicGroup]:
        peer_id, peer_type = chat_id.split("|")

        # 1234567890 | "1234567890"
        if isinstance(peer_id, int) or (isinstance(peer_id, str) and peer_id.isnumeric()):
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="JoinPublicGroup",
                payload=request_pb2.JoinPublicGroup(
                    peer=struct_pb2.Peer(type=int(peer_type), id=int(peer_id))
                )
            )

        # "https://ble.ir/join/ABCDEEFGHI" | "ble.ir/join/ABCDEEFGHI"
        match = search(r'(?:https?://)?ble\.ir/join/([a-zA-Z0-9]+)', peer_id)
        if match:
            token = match.group(1)
        else:    
            token = peer_id

        return await self.invoke(
            service_name="bale.groups.v1.Groups",
            method="JoinGroup",
            payload=request_pb2.JoinGroup(
                token=token
            )
        )
