from .condition import Condition
from ..objects import Message, CallbackQuery


class Author(Condition):
    def __init__(self, *authors):
        super().__init__(can_process=(Message, CallbackQuery))
        self.authors = set(authors)

    async def __call__(self, client, event) -> bool:
        if not event.author:
            return False
        return event.author.id in self.authors
