import balethon
from ...objects import File


class GetFile:

    async def get_file(
            self: "balethon.Client",
            file_id: str
    ) -> File:
        return await self.auto_execute("get", "getFile", locals())
