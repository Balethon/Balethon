class DeleteMessage:

    async def delete_message(self, chat_id, message_id):
        json = locals()
        del json["self"]
        return await self.connection.execute("get", "deleteMessage", json)
