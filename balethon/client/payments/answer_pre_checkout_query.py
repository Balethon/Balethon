import balethon


class AnswerPreCheckoutQuery:
    async def answer_pre_checkout_query(
        self: "balethon.Client",
        pre_checkout_query_id: str,
        ok: bool,
        error_message: str = None,
    ) -> bool:
        return await self.auto_execute("post", "answerPreCheckoutQuery", locals())
