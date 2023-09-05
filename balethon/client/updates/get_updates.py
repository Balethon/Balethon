from ...objects import Update


class GetUpdates:

    async def get_updates(self, offset=None, limit=None):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "getUpdates", json)
        for update in result:
            update = Update.wrap(update)
            update.bind(self)
        return result
