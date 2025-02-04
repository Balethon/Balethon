from .condition import create


@create
def forward(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.forward_from or event.forward_from_chat)
