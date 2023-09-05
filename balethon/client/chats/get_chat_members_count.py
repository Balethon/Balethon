class GetChatMembersCount:

    async def get_chat_members_count(self, chat_id):
        json = locals()
        del json["self"]
        return await self.connection.execute("get", "getChatMembersCount", json)
