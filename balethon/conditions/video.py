from .condition import Condition


@Condition.create
def video(event) -> bool:
    return bool(event.video)
