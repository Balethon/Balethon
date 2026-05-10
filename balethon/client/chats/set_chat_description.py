from typing import Union

import balethon


class SetChatDescription:

    async def set_chat_description(
            self: "balethon.Client",
            chat_id: Union[int, str],
            description: str
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="EditGroupAbout",
                payload=requests.EditGroupAbout(
                    group_peer=structs.GroupOutPeer(group_id=peer_id, access_hash=1),
                    rid=self.ws_connection.create_rid(),
                    about=description
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("setChatDescription", locals())
