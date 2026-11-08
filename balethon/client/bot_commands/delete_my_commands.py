import balethon


class DeleteMyCommands:

    async def delete_my_commands(
            self: "balethon.Client"
    ) -> bool:
        return await self.auto_execute("deleteMyCommands", locals())
