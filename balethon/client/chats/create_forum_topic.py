from typing import Union

import balethon
from ...objects import ForumTopic


class CreateForumTopic:

    async def create_forum_topic(
            self: "balethon.Client",
            chat_id: Union[int, str],
            name: str
    ) -> ForumTopic:
        chat_id = await self.resolve_chat_id(chat_id)
        return await self.auto_execute("createForumTopic", locals())
