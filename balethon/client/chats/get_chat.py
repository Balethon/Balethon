class GetChat:

    async def get_chat(self, chat_id):
        json = {"chat_id": chat_id}
        return await self.connection.execute("get", "getChat", json)
