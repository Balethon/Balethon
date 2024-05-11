from .condition import Condition


@Condition.create
def document(event) -> bool:
    return bool(event.document)
