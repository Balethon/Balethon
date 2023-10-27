import balethon


class InviteUser:

    async def invite_user(
            self: "balethon.Client",
            chat_id: int,
            user_id: int
    ):
        data = locals()
        del data["self"]
        return await self.execute("post", "inviteUser", **data)
