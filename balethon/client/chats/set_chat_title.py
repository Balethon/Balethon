from typing import Union

import balethon


class SetChatTitle:

    async def set_chat_title(
            self: "balethon.Client",
            chat_id: Union[int, str],
            title: str
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs, enums

            if chat_id.peer_id == self.user.id:
                return await self.execute(requests.EditName(name=title))

            return await self.execute(requests.EditGroupTitle(
                group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1),
                title=title,
                rid=self.ws_connection.create_rid()
            ))

        return await self.auto_execute("setChatTitle", locals())
