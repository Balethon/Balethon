from time import time

from .condition import Condition
from ..objects import Message, CallbackQuery


class Restriction(Condition):
    def __init__(self, seconds: float, **authors):
        super().__init__(can_process=(Message, CallbackQuery))
        self.seconds = seconds
        self.authors = authors

    async def __call__(self, client, event):
        current_time = time()
        user_id = str(event.author.id)
        if (
            user_id not in self.authors
            or current_time - self.authors[user_id] >= self.seconds
        ):
            self.authors[user_id] = current_time
            return True
        return False
