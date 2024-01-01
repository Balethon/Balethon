from typing import Union

import balethon
from ...objects import Chat
from ...errors import RPCError


class GetChat:

    async def get_chat(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> Chat:
        data = locals()
        del data["self"]
        if isinstance(chat_id, str) and not chat_id.isnumeric():
            result = {}
            if chat_id.startswith("@"):
                chat_id = chat_id.strip("@")
            elif chat_id.startswith("+"):
                chat_id = "@" + chat_id.strip("+")
            elif not chat_id.isnumeric():
                chat_id = "join/" + chat_id
            info = await self.connection.get_peer_info(chat_id)
            if info["query"].get("token"):
                result["invite_link"] = f"{self.connection.SHORT_URL}/join/{info['query']['token']}"
            info = info["props"]["pageProps"]
            if info["peer"]["type"] == 0:
                raise RPCError.create(404, "no such group or user", "getPeerInfo")
            elif info["peer"]["type"] == 1:
                result["type"] = "private"
                result["username"] = info["user"]["nick"]
                result["first_name"] = info["user"]["title"]
                result["description"] = info["user"]["description"]
            elif info["peer"]["type"] == 2:
                if info["group"]["isChannel"]:
                    result["type"] = "channel"
                    result["username"] = info["group"]["nick"]
                else:
                    result["type"] = "group"
                    result["username"] = "unknown"
                result["title"] = info["group"]["title"]
                result["description"] = info["group"]["description"]
            result["id"] = info["peer"]["id"]
        else:
            result = await self.execute("get", "getChat", **data)
        result = Chat.wrap(result)
        result.bind(self)
        return result
