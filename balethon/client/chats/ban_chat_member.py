import balethon


class BanChatMember:

    async def ban_chat_member(
            self: "balethon.Client",
            chat_id: int,
            user_id: int
    ):
        json = locals()
        del json["self"]
        return await self.execute("post", "banChatMember", json)
