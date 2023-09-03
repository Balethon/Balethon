from ...objects import User


class GetMe:

    async def get_me(self):
        result = await self.connection.execute("get", "getMe")
        return User.wrap(result)
