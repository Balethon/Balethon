import balethon
from ...objects import Update


class GetUpdates:

    async def get_updates(
            self: "balethon.Client",
            offset: int = None,
            limit: int = None
    ):
        data = locals()
        del data["self"]
        result = await self.execute("post", "getUpdates", **data)
        result = [Update.wrap(update) for update in result]
        for update in result:
            update.bind(self)
        return result
