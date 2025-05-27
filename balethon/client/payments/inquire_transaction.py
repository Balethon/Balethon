import balethon
from ...objects import Transaction


class InquireTransaction:
    async def inquire_transaction(self: "balethon.Client", transaction_id: str) -> Transaction:
        return await self.auto_execute("post", "inquireTransaction", locals())
