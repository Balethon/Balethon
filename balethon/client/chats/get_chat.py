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
        if isinstance(chat_id, str) and chat_id.startswith("@"):
            result = {}
            info = await self.connection.get_info_by_username(chat_id.strip("@"))
            result["username"] = info["query"].get("peer") or "unknown"
            if info["query"].get("token"):
                result["invite_link"] = f"{self.connection.SHORT_URL}/join/{info['query']['token']}"
            info = info["props"]["pageProps"]
            if info["peer"]["type"] == 0:
                raise RPCError.create(404, "no such group or user", "getInfoByUsername")
            elif info["peer"]["type"] == 1:
                result["type"] = "private"
                result["first_name"] = info["user"]["title"]
                result["description"] = info["user"]["description"]
            elif info["peer"]["type"] == 2:
                if info["group"]["isChannel"]:
                    result["type"] = "channel"
                else:
                    result["type"] = "group"
                result["title"] = info["group"]["title"]
                result["description"] = info["group"]["description"]
            result["id"] = info["peer"]["id"]
        else:
            result = await self.execute("get", "getChat", **data)
        result = Chat.wrap(result)
        result.bind(self)
        return result
