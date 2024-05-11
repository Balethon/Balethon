from .condition import Condition


@Condition.create
def entities(event) -> bool:
    return bool(event.entities or event.caption_entities)
