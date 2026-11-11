from typing import Union

import balethon


class SetChatDescription:

    async def set_chat_description(
            self: "balethon.Client",
            chat_id: Union[int, str],
            description: str
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs, enums

            if chat_id.peer_id == self.user.id:
                return await self.execute(requests.EditAbout(about=structs.StringValue(value=description)))

            return await self.execute(requests.EditGroupAbout(
                group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1),
                rid=self.ws_connection.create_rid(),
                about=description
            ))

        return await self.auto_execute("setChatDescription", locals())
