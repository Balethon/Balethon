class GetChatMembersCount:

    async def get_chat_members_count(self, chat_id):
        json = {"chat_id": chat_id}
        return await self.connection.execute("get", "getChatMembersCount", json)
