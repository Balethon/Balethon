from ...objects import Chat


class GetChat:

    async def get_chat(self, chat_id):
        json = locals()
        del json["self"]
        result = await self.connection.execute("get", "getChat", json)
        result = Chat.wrap(result)
        result.bind(self)
        return result
