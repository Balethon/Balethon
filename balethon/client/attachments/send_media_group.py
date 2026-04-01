from typing import Union
from json import dumps
from typing import List

import balethon
from ...objects import Message, ReplyMarkup, InputMediaPhoto, InputMediaVideo
from balethon import objects
from ...proto import request_pb2, struct_pb2


class SendMediaGroup:

    async def send_media_group(
            self: "balethon.Client",
            chat_id: Union[int, str],
            media: List["objects.InputMedia"],
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> List[Message]:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            files = []
            for content in media:
                if isinstance(content, InputMediaPhoto):
                    send_type = struct_pb2.SEND_TYPE_PHOTO
                elif isinstance(content, InputMediaVideo):
                    send_type = struct_pb2.SEND_TYPE_VIDEO
                else:
                    send_type = struct_pb2.SEND_TYPE_DOCUMENT
                file = await self.upload_file(f"{peer_id}|{peer_type}", content.media, send_type)

                if send_type == struct_pb2.SEND_TYPE_PHOTO:
                    ext = struct_pb2.DocumentEx(
                        document_ex_photo=struct_pb2.DocumentExPhoto(
                            w=500,
                            h=500
                        )
                    )
                else:
                    ext = struct_pb2.DocumentEx(
                        document_ex_video=struct_pb2.DocumentExVideo(
                            w=500,
                            h=500,
                            duration=10
                        )
                    )

                single_media = struct_pb2.SingleMedia(
                    random_id=self.ws_connection.create_rid(),
                    media=struct_pb2.DocumentMessage(
                        file_id=file.id,
                        access_hash=peer_id,
                        file_size=file.size,
                        name=file.name,
                        mime_type=file.mime_type,
                        ext=ext,
                        caption=struct_pb2.TextMessage(text=content.caption)
                    )
                )
                files.append(single_media)

            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="SendMultiMediaMessage",
                payload=request_pb2.SendMultiMediaMessage(
                    peer=struct_pb2.ExPeer(
                        type=peer_type,
                        id=peer_id,
                    ),
                    multi_media=files,
                    grouped_id=self.ws_connection.create_rid(),
                )
            )

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
        result = await self.execute("sendMediaGroup", **data)
        result = [Message.wrap(message) for message in result]
        for message in result:
            message.bind(self)
        return result
