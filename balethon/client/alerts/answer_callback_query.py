import balethon


class AnswerCallbackQuery:
    async def asnwer_callback_query(
        self: "balethon.Client",
        callback_query_id: str,
        text: str = None,
        show_alert: bool = None,
    ) -> bool:
        return await self.auto_execute("post", "answerCallbackQuery", locals())
    