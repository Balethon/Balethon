import balethon
from ...objects import File


class GetFile:

    async def get_file(
            self: "balethon.Client",
            file_id: str
    ) -> File:
        if self.is_userbot():
            from ...proto import requests, structs
            access_hash, file_id, file_storage_version = map(int, file_id.split(":"))
            return await self.execute(requests.GetNasimFileUrl(
                file=structs.FileLocation(
                    file_id=file_id,
                    access_hash=access_hash,
                    file_storage_version=structs.Int32Value(value=file_storage_version)
                )
            ))

        return await self.auto_execute("getFile", locals())
