from .condition import Condition


@Condition.create
def forward(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.forward_from or event.forward_from_chat)
