import balethon


class GetChatMembersCount:

    async def get_chat_members_count(
            self: "balethon.Client",
            chat_id: int
    ):
        data = locals()
        del data["self"]
        return await self.execute("get", "getChatMembersCount", **data)
