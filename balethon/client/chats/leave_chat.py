import balethon


class LeaveChat:

    async def leave_chat(
            self: "balethon.Client",
            chat_id: int
    ):
        data = locals()
        del data["self"]
        return await self.execute("post", "leaveChat", **data)
