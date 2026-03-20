import balethon
from ...objects import File
from ...proto import request_pb2, struct_pb2


class GetFile:

    async def get_file(
            self: "balethon.Client",
            file_id: str
    ) -> File:
        if self.is_userbot():
            access_hash, file_id, file_storage_version = map(int, file_id.split(":"))
            return await self.invoke(
                service_name="ai.bale.server.Files",
                method="GetNasimFileUrl",
                payload=request_pb2.GetNasimFileUrl(
                    file=struct_pb2.FileLocation(
                        file_id=file_id,
                        access_hash=access_hash,
                        file_storage_version=file_storage_version
                    )
                )
            )

        return await self.auto_execute("getFile", locals())
