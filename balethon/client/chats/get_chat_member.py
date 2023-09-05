from ...objects import ChatMember


class GetChatMember:

    async def get_chat_member(self, chat_id, user_id):
        json = locals()
        del json["self"]
        result = await self.connection.execute("get", "getChatMember", json)
        result = ChatMember.wrap(result)
        result.bind(self)
        return result
