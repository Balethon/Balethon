from .condition import Condition


@Condition.create
def photo(event) -> bool:
    return bool(event.photo)
