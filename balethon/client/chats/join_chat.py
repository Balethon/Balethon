from typing import Union

import balethon
try:
    from ...proto import requests, structs, responses
except ImportError:
    pass


class JoinChat:
    async def join_chat(
            self: "balethon.Client",
            chat_id: str
    ) -> Union["responses.JoinGroup", "responses.JoinPublicGroup"]:
        chat_id = await self.resolve_chat_id(chat_id)

        # 1234567890 | "1234567890"
        if isinstance(chat_id.peer_id, int) or (isinstance(chat_id.peer_id, str) and chat_id.peer_id.isnumeric()):
            return await self.execute(requests.JoinPublicGroup(
                peer=structs.Peer(type=int(chat_id.peer_type), id=int(chat_id.peer_id))
            ))

        # "https://ble.ir/join/ABCDEEFGHI" | "ble.ir/join/ABCDEEFGHI" 
        token = peer_id.replace("https://", "").replace("ble.ir/join/", "")

        return await self.execute(requests.JoinGroup(
            token=token
        ))
