import balethon


class DeleteMessage:

    async def delete_message(
            self: "balethon.Client",
            chat_id: int,
            message_id: int
    ):
        json = locals()
        del json["self"]
        return await self.execute("get", "deleteMessage", json)
