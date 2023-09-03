from ...objects import Update


class GetUpdates:

    async def get_updates(self, offset=None, limit=None):
        json = {"offset": offset, "limit": limit}
        result = await self.connection.execute("post", "getUpdates", json)
        return [Update.wrap(update) for update in result]
