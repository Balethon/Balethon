from typing import Union

import balethon
from balethon import enums


class SendChatAction:

    async def send_chat_action(
            self: "balethon.Client",
            chat_id: Union[int, str],
            action: "enums.ChatAction" = enums.ChatAction.TYPING
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from ...proto import requests, structs
            return await self.execute(requests.Typing(
                peer=structs.OutPeer(type=chat_id.peer_type, id=chat_id.peer_id),
                typing_type=action.to_protobuf(),
            ))

        chat_id = str(chat_id)  # The sendChatAction method only works with a string chat_id
        return await self.auto_execute("sendChatAction", locals())
