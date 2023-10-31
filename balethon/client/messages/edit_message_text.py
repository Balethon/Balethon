from typing import Union

import balethon
from ...objects import Object, Message
from balethon import objects


class EditMessageText:

    async def edit_message_text(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: int,
            text: str,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        for key, value in data.copy().items():
            if isinstance(value, Object):
                data[key] = value.unwrap()
        result = await self.execute("post", "editMessageText", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
