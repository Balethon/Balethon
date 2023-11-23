import balethon
from ...objects import File


class GetFile:

    async def get_file(
            self: "balethon.Client",
            file_id: str
    ) -> File:
        data = locals()
        del data["self"]
        result = await self.execute("get", "getFile", **data)
        result = File.wrap(result)
        result.bind(self)
        return result
