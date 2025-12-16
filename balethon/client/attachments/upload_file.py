from httpx import AsyncClient

import balethon
from ...proto.response_pb2 import GetNasimFileUploadUrl
from balethon.proto import request_pb2, struct_pb2


class UploadFile:

    async def upload_file(
            self: "balethon.Client",
            chat_id: str,
            file: bytes,
            expected_size: int,
            name: str,
            mime_type: str,
            send_type: "struct_pb2.SendType",
    ) -> GetNasimFileUploadUrl:
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
        
        async with AsyncClient(http2=True) as client:
            response = await client.put(
                result.url,
                content=file
            )
            return result if response.is_success else None
