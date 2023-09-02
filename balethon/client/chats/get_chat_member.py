class GetChatMember:

    async def get_chat_member(self, chat_id, user_id):
        json = {"chat_id": chat_id, "user_id": user_id}
        return await self.connection.execute("get", "getChatMember", json)
