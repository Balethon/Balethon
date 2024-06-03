from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia


class UploadStickerFile:

    async def upload_sticker_file(
            self: "balethon.Client",
            user_id: Union[int, str],
            sticker: Union[str, bytes, BinaryIO, InputMedia]
    ) -> str:
        user_id = await self.resolve_peer_id(user_id)
        if not isinstance(sticker, InputMedia):
            sticker = InputMedia(media=sticker)
        sticker = sticker.media
        data = locals()
        del data["self"]
        result = await self.execute("get", "uploadStickerFile", **data)
        return result
