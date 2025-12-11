from typing import Union

import balethon
from balethon.proto import request_pb2, struct_pb2


class SetChatTitle:

    async def set_chat_title(
            self: "balethon.Client",
            chat_id: Union[int, str],
            title: str
    ) -> bool:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="EditGroupTitle",
                payload=request_pb2.EditGroupTitle(
                    group_peer=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1),
                    title=title,
                    rid=self.connection.create_rid()
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("setChatTitle", locals())
