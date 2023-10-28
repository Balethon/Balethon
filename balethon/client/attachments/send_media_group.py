from json import dumps
from typing import List

import balethon
from ...objects import Message
from balethon import objects


class SendMediaGroup:

    async def send_media_group(
            self: "balethon.Client",
            chat_id: int,
            media: List["objects.InputMedia"]
    ):
        data = locals()
        del data["self"]
        for i, m in enumerate(data["media"]):
            data[m] = open(m, "rb")
            data["media"][i] = {"type": "photo", "media": f"attach://{m}"}
        data["media"] = dumps(data["media"])
        result = await self.execute("post", "sendMediaGroup", json=False, **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
