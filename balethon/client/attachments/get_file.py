from ...objects import File


class GetFile:

    async def get_file(self, file_id):
        json = {"file_id": file_id}
        result = await self.connection.execute("get", "getFile", json)
        return File.wrap(result)
