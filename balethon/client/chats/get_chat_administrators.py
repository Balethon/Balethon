from ...objects import ChatMember


class GetChatAdministrators:

    async def get_chat_administrators(self, chat_id):
        json = {"chat_id": chat_id}
        result = await self.connection.execute("get", "getChatAdministrators", json)
        return [ChatMember.wrap(chat_administrator) for chat_administrator in result]
