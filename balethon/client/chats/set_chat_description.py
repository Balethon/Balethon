from typing import Union

import balethon


class SetChatDescription:

    async def set_chat_description(
            self: "balethon.Client",
            chat_id: Union[int, str],
            description: str
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import requests, structs, enums
            peer_id, peer_type = map(int, chat_id.split("|"))

            if peer_id == self.user.id and peer_type == enums.ExPeerType.EX_PEER_TYPE_PRIVATE:
                return await self.execute(requests.EditAbout(about=structs.StringValue(value=description)))

            return await self.execute(requests.EditGroupAbout(
                group_peer=structs.GroupOutPeer(group_id=peer_id, access_hash=1),
                rid=self.ws_connection.create_rid(),
                about=description
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("setChatDescription", locals())
