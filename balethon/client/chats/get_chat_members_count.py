import balethon


class GetChatMembersCount:

    async def get_chat_members_count(
            self: "balethon.Client",
            chat_id: int
    ):
        json = locals()
        del json["self"]
        return await self.connection.execute("get", "getChatMembersCount", json)
