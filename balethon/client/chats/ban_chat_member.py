import balethon


class BanChatMember:

    async def ban_chat_member(
            self: "balethon.Client",
            chat_id: int,
            user_id: int
    ):
        data = locals()
        del data["self"]
        return await self.execute("post", "banChatMember", **data)
