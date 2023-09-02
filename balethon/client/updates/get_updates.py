class GetUpdates:

    async def get_updates(self, offset=None, limit=None):
        json = {"offset": offset, "limit": limit}
        return await self.connection.execute("post", "getUpdates", json)
