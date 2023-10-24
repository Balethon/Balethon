import balethon


class LeaveChat:

    async def leave_chat(
            self: "balethon.Client",
            chat_id: int
    ):
        json = locals()
        del json["self"]
        return await self.execute("post", "leaveChat", json)
