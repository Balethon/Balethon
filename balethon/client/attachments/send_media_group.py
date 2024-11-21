from typing import Union
from json import dumps
from typing import List

import balethon
from ...objects import Message
from balethon import objects


class SendMediaGroup:

    async def send_media_group(
            self: "balethon.Client",
            chat_id: Union[int, str],
            media: List["objects.InputMedia"]
    ) -> List[Message]:
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        if any(not m.is_json_serializable for m in data["media"]):
            for i, m in enumerate(data["media"]):
                data["media"][i] = m.unwrap()
                if not m.is_json_serializable:
                    data[f"media{i}"] = m.media
                    data["media"][i]["media"] = f"media{i}"
            data["media"] = dumps(data["media"])
        else:
            for i, m in enumerate(data["media"]):
                data["media"][i] = m.unwrap()
        result = await self.execute("post", "sendMediaGroup", **data)
        result = [Message.wrap(message) for message in result]
        for message in result:
            message.bind(self)
        return result
