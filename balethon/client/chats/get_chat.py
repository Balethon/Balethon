import balethon
from ...objects import Chat


class GetChat:

    async def get_chat(
            self: "balethon.Client",
            chat_id: int
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("get", "getChat", json)
        result = Chat.wrap(result)
        result.bind(self)
        return result
