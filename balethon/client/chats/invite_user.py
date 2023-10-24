import balethon


class InviteUser:

    async def invite_user(
            self: "balethon.Client",
            chat_id: int,
            user_id: int
    ):
        json = locals()
        del json["self"]
        return await self.execute("post", "inviteUser", json)
