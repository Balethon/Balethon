from .condition import Condition
from ..objects import Message, CallbackQuery
from ..states import State


class AtState(Condition):
    def __init__(self, state, state_machine=None):
        super().__init__(can_process=(Message, CallbackQuery))
        self.state = str(state) if isinstance(state, State) else state
        self.state_machine = state_machine

    async def __call__(self, client, event) -> bool:
        if not event.author:
            return False
        if self.state_machine is None:
            return event.author.get_state() == self.state
        else:
            return self.state_machine[event.author.id] == self.state
