from ...objects import Chat


class GetChat:

    async def get_chat(self, chat_id):
        json = {"chat_id": chat_id}
        result = await self.connection.execute("get", "getChat", json)
        return Chat.wrap(result)
