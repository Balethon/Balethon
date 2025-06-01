from typing import Union

import balethon
from ...objects import Chat
from ...errors import RPCError
from ...enums import ChatType


class GetChat:

    async def get_chat(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> Chat:
        result = Chat()
        
        # 1234567890 | "1234567890"
        if isinstance(chat_id, int) or (
            isinstance(chat_id, str) and chat_id.isnumeric()
        ):
            info = await self.auto_execute("get", "getChat", locals())
            result.id = info.id
            result.username = info.username
            result.description = info.description
            
            if info.type == "private":
                result.type = ChatType.PRIVATE
                result.first_name = info.first_name
                result.bind(self)
                return result
            
            result.title = info.title
            if info.type == "group":
                result.type = ChatType.GROUP
            if info.type == "channel":
                result.type = ChatType.CHANNEL
            result.bind(self)
            return result
            
        # "@username"
        if chat_id.startswith("@"):
            chat_id = chat_id.lstrip("@")

        # "+9*********" | "+09*********" | "+989*********"
        elif chat_id.startswith("+"):
            chat_id = "@" + chat_id.lstrip("+")

        # "https://ble.ir/join/ABCDEEFGHI" | "https://ble.ir/username"
        elif chat_id.startswith(f"{self.connection.SHORT_URL}/"):
            chat_id = chat_id.replace(f"{self.connection.SHORT_URL}/", "")

        # "ble.ir/join/ABCDEEFGHI" | "ble.ir/username"
        elif chat_id.startswith("ble.ir/"):
            chat_id = chat_id.replace("ble.ir/", "")

        info = await self.connection.get_peer_info(chat_id)

        if info["query"].get("token"):
            token = info["query"]["token"]
            result.invite_link = f"{self.connection.SHORT_URL}/join/{token}"

        info = info["props"]["pageProps"]

        if info["peer"]["type"] == 0:
            raise RPCError.create(code=404, description="no such group or user", reason="getChat")

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
