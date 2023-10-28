from json import dumps

import balethon
from balethon.objects import Message


class SendMediaGroup:

    async def send_media_group(
            self: "balethon.Client",
            chat_id: int,
            media: list
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
