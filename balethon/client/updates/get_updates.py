from typing import List

import balethon
from ...objects import Update


class GetUpdates:

    async def get_updates(
            self: "balethon.Client",
            offset: int = None,
            limit: int = None
    ) -> List[Update]:
        return await self.auto_execute("post", "getUpdates", locals())
