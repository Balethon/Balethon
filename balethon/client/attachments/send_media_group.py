import balethon
from balethon.objects import Object, Message
from balethon import objects


class SendMediaGroup:

    async def send_media_group(
            self: "balethon.Client",
            chat_id: int,
            media: list
    ):
        json = locals()
        del json["self"]
        for key, value in json.copy().items():
            if isinstance(value, Object):
                json[key] = value.unwrap()
        result = await self.execute("post", "sendMediaGroup", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
