from .condition import Condition


@Condition.create
def forward(event) -> bool:
    return bool(event.forward_from or event.forward_from_chat)
