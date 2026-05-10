from typing import Union
from json import dumps
from typing import List

import balethon
from ...objects import Message, ReplyMarkup, InputMediaPhoto, InputMediaVideo
from balethon import objects


class SendMediaGroup:

    async def send_media_group(
            self: "balethon.Client",
            chat_id: Union[int, str],
            media: List["objects.InputMedia"],
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> List[Message]:
        if self.is_userbot():
            from ...proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            files = []
            for content in media:
                if isinstance(content, InputMediaPhoto):
                    send_type = structs.SEND_TYPE_PHOTO
                elif isinstance(content, InputMediaVideo):
                    send_type = structs.SEND_TYPE_VIDEO
                else:
                    send_type = structs.SEND_TYPE_DOCUMENT
                file = await self.upload_file(f"{peer_id}|{peer_type}", content.media, send_type)

                if send_type == structs.SEND_TYPE_PHOTO:
                    ext = structs.DocumentEx(
                        document_ex_photo=structs.DocumentExPhoto(
                            w=500,
                            h=500
                        )
                    )
                else:
                    ext = structs.DocumentEx(
                        document_ex_video=structs.DocumentExVideo(
                            w=500,
                            h=500,
                            duration=10
                        )
                    )

                single_media = structs.SingleMedia(
                    random_id=self.ws_connection.create_rid(),
                    media=structs.DocumentMessage(
                        file_id=file.id,
                        access_hash=peer_id,
                        file_size=file.size,
                        name=file.name,
                        mime_type=file.mime_type,
                        ext=ext,
                        caption=structs.TextMessage(text=content.caption)
                    )
                )
                files.append(single_media)

            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="SendMultiMediaMessage",
                payload=requests.SendMultiMediaMessage(
                    peer=structs.ExPeer(
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
