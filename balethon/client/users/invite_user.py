from typing import Union

import balethon


class InviteUser:

    async def invite_user(
            self: "balethon.Client",
            chat_id: Union[int, str],
            user_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="InviteUsers",
                payload=requests.InviteUsers(
                    group_peer=structs.GroupOutPeer(group_id=peer_id, access_hash=1),
                    rid=self.ws_connection.create_rid(),
                    users=[structs.UserOutPeer(uid=user_id, access_hash=1)]
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        user_id = await self.resolve_peer_id(user_id)
        return await self.auto_execute("inviteUser", locals())
