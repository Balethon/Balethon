from typing import Union

import balethon


class EditForumTopic:

    async def edit_forum_topic(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_thread_id: int,
            name: str
    ) -> bool:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("editForumTopic", locals())
