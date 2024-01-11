from .condition import Condition


@Condition.create
async def forward(condition, client, message) -> bool:
    bool(message.forward_from or message.forward_from_chat)
