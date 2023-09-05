import balethon
from ...objects import Update


class GetUpdates:

    async def get_updates(
            self: "balethon.Client",
            offset: int = None,
            limit: int = None
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "getUpdates", json)
        result = [Update.wrap(update) for update in result]
        for update in result:
            update.bind(self)
        return result
