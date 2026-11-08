from typing import List

import balethon
from ...objects import BotCommand


class SetMyCommands:

    async def set_my_commands(
            self: "balethon.Client",
            commands: List[BotCommand]
    ) -> bool:
        return await self.auto_execute("setMyCommands", locals())
