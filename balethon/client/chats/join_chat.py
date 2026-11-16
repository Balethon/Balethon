from typing import Union

import balethon
from ...objects import ChatId
try:
    from ...proto import requests, structs, responses
except ImportError:
    pass


class JoinChat:
    async def join_chat(
            self: "balethon.Client",
            chat_id: str
    ) -> Union["responses.JoinGroup", "responses.JoinPublicGroup"]:
        if isinstance(chat_id, str) and chat_id.startswith(("https://ble.ir/join/", "ble.ir/join/")):
            # "https://ble.ir/join/ABCDEEFGHI" | "ble.ir/join/ABCDEEFGHI"
            token = chat_id.removeprefix("https://").removeprefix("ble.ir/join/")
            return await self.execute(requests.JoinGroup(token=token))

        chat_id = await self.resolve_chat_id(chat_id)

        return await self.execute(requests.JoinPublicGroup(
            peer=structs.Peer(type=int(chat_id.peer_type), id=int(chat_id.peer_id))
        ))
