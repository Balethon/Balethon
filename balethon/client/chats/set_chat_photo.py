from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia


class SetChatPhoto:

    async def set_chat_photo(
            self: "balethon.Client",
            chat_id: Union[int, str],
            photo: Union[str, bytes, BinaryIO, InputMedia]
    ) -> bool:
        chat_id = await self.resolve_peer_id(chat_id)
        if not isinstance(photo, InputMedia):
            photo = InputMedia(media=photo)
        photo = photo.media
        data = locals()
        del data["self"]
        return await self.execute("post", "setChatPhoto", json=False, **data)
