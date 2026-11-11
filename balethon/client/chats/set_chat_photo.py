from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media


class SetChatPhoto:

    async def set_chat_photo(
            self: "balethon.Client",
            chat_id: Union[int, str],
            photo: Union[str, bytes, BinaryIO, InputMedia]
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)
        photo = resolve_media(photo)

        if self.is_userbot():
            from ...proto import requests, structs, enums
            file = await self.upload_file(f"{self.user.id}:1", photo, enums.SEND_TYPE_PHOTO)
            file_location = structs.FileLocation(file_id=file.id, access_hash=self.user.id)

            if chat_id.peer_id == self.user.id:
                return await self.execute(requests.EditAvatar(file_location=file_location))

            return await self.execute(requests.EditGroupAvatar(
                group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1),
                file_location=file_location,
                rid=self.ws_connection.create_rid()
            ))

        return await self.auto_execute("setChatPhoto", locals())
