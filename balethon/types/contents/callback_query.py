from ..object import Object


class CallbackQuery(Object):

    @classmethod
    def from_dict(cls, client, callback_query_dict):
        if callback_query_dict.get("from"):
            callback_query_dict["from_user"] = callback_query_dict.pop("from")
        callback_query_dict["client"] = client
        return cls(**callback_query_dict)

    def __init__(
            self,
            id=None,
            from_user=None,
            message=None,
            inline_message_id=None,
            chat_instance=None,
            data=None,
            game_short_name=None,
            client=None,
            **kwarg
    ):
        super().__init__(client)
        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

    async def answer(self, text, reply_markup=None, reply_to_message_id=None):
        await self.client.send_message(self.message["chat"]["id"], text, reply_markup, reply_to_message_id)
