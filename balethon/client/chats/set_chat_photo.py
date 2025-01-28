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
        return await self.auto_execute("post", "setChatPhoto", locals())
