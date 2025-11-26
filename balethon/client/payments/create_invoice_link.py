from typing import List

import balethon
from ...objects import LabeledPrice


class CreateInvoiceLink:

    async def create_invoice_link(
            self: "balethon.Client",
            title: str,
            description: str,
            payload: str,
            provider_token: str,
            prices: List[LabeledPrice],
            **kwargs
    ) -> str:
        return await self.auto_execute("createInvoiceLink", locals())
