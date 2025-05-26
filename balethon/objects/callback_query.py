from . import Object
from balethon import objects
from ..sync_support import add_sync_support_to_object


@add_sync_support_to_object
class CallbackQuery(Object):
    attribute_names = [
        ("author", "from")
    ]

    def __init__(
            self,
            id: str = None,
            author: "objects.User" = None,
            message: "objects.Message" = None,
            inline_message_id: str = None,
            chat_instance: str = None,
            data: str = None,
            game_short_name: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.author: "objects.User" = author
        self.message: "objects.Message" = message
        self.inline_message_id: str = inline_message_id
        self.chat_instance: str = chat_instance
        self.data: str = data
        self.game_short_name: str = game_short_name

    async def answer(
            self,
            text: str,
            show_alert: bool = None
    ):
        return await self.client.execute(
            "post",
            "answerCallbackQuery",
            callback_query_id=self.id,
            text=text,
            show_alert=show_alert,
        )
