class GetMe:

    async def get_me(self):
        return await self.connection.execute("get", "getMe")
