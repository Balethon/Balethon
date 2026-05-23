from typing import Union

import balethon


class LeaveChat:

    async def leave_chat(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.execute(requests.LeaveGroup(
                group_peer=structs.GroupOutPeer(group_id=peer_id, access_hash=1),
                rid=self.ws_connection.create_rid(),
                make_orphan=False
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("leaveChat", locals())
