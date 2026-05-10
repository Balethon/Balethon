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
        peer_id, peer_type = chat_id.split("|")

        # 1234567890 | "1234567890"
        if isinstance(peer_id, int) or (isinstance(peer_id, str) and peer_id.isnumeric()):
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="JoinPublicGroup",
                payload=requests.JoinPublicGroup(
                    peer=structs.Peer(
                        type=int(peer_type),
                        id=int(peer_id)
                    )
                )
            )

        # "https://ble.ir/join/ABCDEEFGHI" | "ble.ir/join/ABCDEEFGHI" 
        token = peer_id.replace("https://", "").replace("ble.ir/join/", "")

        return await self.invoke(
            service_name="bale.groups.v1.Groups",
            method="JoinGroup",
            payload=requests.JoinGroup(
                token=token
            )
        )
