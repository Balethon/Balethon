import balethon
from ...objects import Chat


class GetChat:

    async def get_chat(
            self: "balethon.Client",
            chat_id: int
    ):
        data = locals()
        del data["self"]
        result = await self.execute("get", "getChat", **data)
        result = Chat.wrap(result)
        result.bind(self)
        return result
