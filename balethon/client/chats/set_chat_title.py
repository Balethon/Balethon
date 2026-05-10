from typing import Union

import balethon


class SetChatTitle:

    async def set_chat_title(
            self: "balethon.Client",
            chat_id: Union[int, str],
            title: str
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="EditGroupTitle",
                payload=requests.EditGroupTitle(
                    group_peer=structs.GroupOutPeer(group_id=peer_id, access_hash=1),
                    title=title,
                    rid=self.ws_connection.create_rid()
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("setChatTitle", locals())
