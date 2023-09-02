class GetChatAdministrators:

    async def get_chat_administrators(self, chat_id):
        json = {"chat_id": chat_id}
        return await self.connection.execute("get", "getChatAdministrators", json)
