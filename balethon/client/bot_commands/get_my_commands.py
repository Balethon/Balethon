from typing import List

import balethon
from ...objects import BotCommand


class GetMyCommands:

    async def get_my_commands(
            self: "balethon.Client"
    ) -> List[BotCommand]:
        return await self.auto_execute("getMyCommands", locals())
