from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media
from ...proto import request_pb2, struct_pb2


class SetChatPhoto:

    async def set_chat_photo(
            self: "balethon.Client",
            chat_id: Union[int, str],
            photo: Union[str, bytes, BinaryIO, InputMedia]
    ) -> bool:
        photo = resolve_media(photo)

        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            file = await self.upload_file(f"{self.user.id}|1", photo, struct_pb2.SEND_TYPE_PHOTO)
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="EditGroupAvatar",
                payload=request_pb2.EditGroupAvatar(
                    group_peer=struct_pb2.GroupOutPeer(
                        group_id=peer_id,
                        access_hash=1
                    ),
                    file_location=struct_pb2.FileLocation(
                        file_id=file.id,
                        access_hash=self.user.id
                    ),
                    rid=self.ws_connection.create_rid()
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("setChatPhoto", locals())
