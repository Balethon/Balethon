from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media


class SetChatPhoto:

    async def set_chat_photo(
            self: "balethon.Client",
            chat_id: Union[int, str],
            photo: Union[str, bytes, BinaryIO, InputMedia]
    ) -> bool:
        photo = resolve_media(photo)

        if self.is_userbot():
            from ...proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            file = await self.upload_file(f"{self.user.id}|1", photo, structs.SEND_TYPE_PHOTO)
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="EditGroupAvatar",
                payload=requests.EditGroupAvatar(
                    group_peer=structs.GroupOutPeer(
                        group_id=peer_id,
                        access_hash=1
                    ),
                    file_location=structs.FileLocation(
                        file_id=file.id,
                        access_hash=self.user.id
                    ),
                    rid=self.ws_connection.create_rid()
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("setChatPhoto", locals())
