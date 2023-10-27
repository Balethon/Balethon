import balethon
from balethon.objects import Object, Message
from balethon import objects


class SendMediaGroup:

    async def send_media_group(
            self: "balethon.Client",
            chat_id: int,
            media: list
    ):
        data = locals()
        del data["self"]
        for key, value in data.copy().items():
            if isinstance(value, Object):
                data[key] = value.unwrap()
        result = await self.execute("post", "sendMediaGroup", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
