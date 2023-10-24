import balethon
from ...objects import File


class GetFile:

    async def get_file(
            self: "balethon.Client",
            file_id: str
    ):
        json = locals()
        del json["self"]
        result = await self.execute("get", "getFile", json)
        result = File.wrap(result)
        result.bind(self)
        return result
