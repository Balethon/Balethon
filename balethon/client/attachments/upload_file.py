import balethon
from ...network import HTTP2Conection
from balethon.proto import request_pb2, struct_pb2


class UploadFile:

    async def upload_file(
            self: "balethon.Client",
            chat_id: str,
            file: bytes,
            expected_size: int,
            name: str,
            mime_type: str,
            send_type: "struct_pb2.SendType"
    ) -> int:
        peer_id, peer_type = map(int, chat_id.split("|"))
        result = await self.invoke(
            service_name="ai.bale.server.Files",
            method="GetNasimFileUploadUrl",
            payload=request_pb2.GetNasimFileUploadUrl(
                expected_size=expected_size,
                crc=0,
                uid=peer_id,
                name=name,
                mime_type=mime_type,
                ex_peer=struct_pb2.ExPeer(
                    type=peer_type,
                    id=peer_id,
                    access_hash=0
                ),
                send_type=struct_pb2.SendTypeValue(
                    type=send_type
                )
            )
        )
        if not result:
            return
        connection = HTTP2Conection()
        is_uploaded = await connection.upload_file(result.url, file)
        if is_uploaded:
            return result.file_id
