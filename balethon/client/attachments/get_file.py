class GetFile:

    async def get_file(self, file_id):
        json = {"file_id": file_id}
        return await self.connection.execute("get", "getFile", json)
