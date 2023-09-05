from ...objects import ChatMember


class GetChatAdministrators:

    async def get_chat_administrators(self, chat_id):
        json = locals()
        del json["self"]
        result = await self.connection.execute("get", "getChatAdministrators", json)
        result = [ChatMember.wrap(chat_administrator) for chat_administrator in result]
        for chat_administrator in result:
            chat_administrator.bind(self)
        return result
