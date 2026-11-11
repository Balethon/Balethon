from typing import Union

import balethon


class DeleteForumTopic:

    async def delete_forum_topic(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_thread_id: int
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)
        return await self.auto_execute("deleteForumTopic", locals())
