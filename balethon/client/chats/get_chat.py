from typing import Union

import balethon
from ...objects import Chat
from ...enums import ChatType


class GetChat:

    async def get_chat(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> Chat:
        # 1234567890 | "1234567890"
        if isinstance(chat_id, int) or (isinstance(chat_id, str) and chat_id.isnumeric()):
            return await self.auto_execute("post", "getChat", locals())

        query = chat_id

        # "@username"
        if query.startswith("@"):
            query = query.lstrip("@")

        # "+9*********" | "+09*********" | "+989*********"
        elif query.startswith("+"):
            query = "@" + query.lstrip("+")

        # "https://ble.ir/join/ABCDEEFGHI" | "https://ble.ir/username"
        elif query.startswith(f"{self.connection.SHORT_URL}/"):
            query = query.replace(f"{self.connection.SHORT_URL}/", "")

        # "ble.ir/join/ABCDEEFGHI" | "ble.ir/username"
        elif query.startswith("ble.ir/"):
            query = query.replace("ble.ir/", "")

        info = await self.connection.get_peer_info(query)

        result = Chat()

        if info["query"].get("token"):
            token = info["query"]["token"]
            result.invite_link = f"{self.connection.SHORT_URL}/join/{token}"

        info = info["props"]["pageProps"]

        if info["peer"]["type"] == 0:
            return await self.auto_execute("post", "getChat", locals())

        elif info["peer"]["type"] == 1:
            result.type = ChatType.PRIVATE
            result.username = info["user"]["nick"] if info["user"].get("nick") else None
            result.first_name = info["user"]["title"]
            result.description = info["user"]["description"]

        elif info["peer"]["type"] == 2:
            result.type = ChatType.CHANNEL if info["group"]["isChannel"] else ChatType.GROUP
            result.username = info["group"]["nick"] if info["group"].get("nick") else None
            result.title = info["group"]["title"]
            result.description = info["group"]["description"]

        result.id = info["peer"]["id"]
        result.bind(self)
        return result
