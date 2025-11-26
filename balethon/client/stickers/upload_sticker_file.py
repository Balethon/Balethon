from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media


class UploadStickerFile:

    async def upload_sticker_file(
            self: "balethon.Client",
            user_id: Union[int, str],
            sticker: Union[str, bytes, BinaryIO, InputMedia]
    ) -> str:
        user_id = await self.resolve_peer_id(user_id)
        sticker = resolve_media(sticker)
        return await self.auto_execute("uploadStickerFile", locals())
