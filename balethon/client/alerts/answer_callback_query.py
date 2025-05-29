import balethon


class AnswerCallbackQuery:
    async def asnwer_callback_query(
        self: "balethon.Client",
        callback_query_id: str,
        text: str,
        show_alert: bool = False,
    ) -> bool:
        return await self.auto_execute("post", "answerCallbackQuery", locals())
