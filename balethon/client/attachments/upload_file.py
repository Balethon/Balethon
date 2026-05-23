from typing import Union, BinaryIO
from io import BufferedIOBase, BytesIO, RawIOBase
import mimetypes
import os

import balethon
from ...objects import File
try:
    from balethon.proto import requests, structs, enums
except ImportError:
    pass


class UploadFile:

    async def upload_file(
            self: "balethon.Client",
            chat_id: str,
            file: Union[bytes, BinaryIO],
            send_type: "enums.SendType",
            expected_size: int = None,
            name: str = None,
            mime_type: str = None,
    ) -> File:
        peer_id, peer_type = map(int, chat_id.split("|"))

        is_file_like = isinstance(file, (BufferedIOBase, BytesIO, RawIOBase))

        if not expected_size:
            if isinstance(file, bytes):
                expected_size = len(file)
            elif is_file_like:
                current = file.tell()
                file.seek(0, 2)
                expected_size = file.tell()
                file.seek(current)

        if not name:
            if is_file_like:
                raw_name = getattr(file, "name", None)
                name = os.path.basename(raw_name) if raw_name else "upload"
            else:
                name = "upload"

        send_type_map = {
            enums.SEND_TYPE_PHOTO: "image",
            enums.SEND_TYPE_VIDEO: "video",
            enums.SEND_TYPE_GIF: "video",
            enums.SEND_TYPE_AUDIO: "audio",
            enums.SEND_TYPE_VOICE: "audio",
            enums.SEND_TYPE_DOCUMENT: "document",
        }
        file_type = send_type_map.get(send_type, "application")

        if not mime_type:
            if name != "upload":
                mime_type = mimetypes.guess_type(name)[0]

        if not mime_type:
            mime_type = f"{file_type}/octet-stream"

        if is_file_like:
            file.seek(0)
            file = file.read()

        result = await self.execute(requests.GetNasimFileUploadUrl(
            expected_size=expected_size,
            crc=0,
            uid=peer_id,
            name=name,
            mime_type=mime_type,
            ex_peer=structs.ExPeer(
                type=peer_type,
                id=peer_id,
                access_hash=0
            ),
            send_type=structs.SendTypeValue(
                type=send_type
            )
        ))
        await self.http2_connection.upload_file(result.url, file, result.chunk_size)
        return File(id=result.file_id, size=expected_size, name=name, mime_type=mime_type)
