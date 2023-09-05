from ...objects import File


class GetFile:

    async def get_file(self, file_id):
        json = locals()
        del json["self"]
        result = await self.connection.execute("get", "getFile", json)
        result = File.wrap(result)
        result.bind(self)
        return result
