class DeleteMessage:

    async def delete_message(self, chat_id, message_id):
        json = {"chat_id": chat_id, "message_id": message_id}
        return await self.connection.execute("get", "deleteMessage", json)
