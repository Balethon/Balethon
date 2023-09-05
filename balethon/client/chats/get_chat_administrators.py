from ...objects import ChatMember


class GetChatAdministrators:

    async def get_chat_administrators(self, chat_id):
        json = locals()
        del json["self"]
        result = await self.connection.execute("get", "getChatAdministrators", json)
        for chat_administrator in result:
            chat_administrator = ChatMember.wrap(chat_administrator)
            chat_administrator.bind(self)
        return result
