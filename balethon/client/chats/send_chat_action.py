from typing import Union

import balethon
from balethon import enums
from ...proto import request_pb2, struct_pb2


class SendChatAction:

    async def send_chat_action(
            self: "balethon.Client",
            chat_id: Union[int, str],
            action: "enums.ChatAction" = enums.ChatAction.TYPING
    ) -> bool:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.invoke(
                service_name="bale.presence.v1.Presence",
                method="Typing",
                payload=request_pb2.Typing(
                    peer=struct_pb2.OutPeer(
                        type=peer_type,
                        id=peer_id,
                    ),
                    typing_type=action,
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        chat_id = str(chat_id)  # The sendChatAction method only works with a string chat_id
        return await self.auto_execute("sendChatAction", locals())
