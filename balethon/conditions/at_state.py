from .condition import Condition
from ..objects import Object


class AtState(Condition):
    def __init__(self, state, state_machine=None):
        super().__init__()
        self.state = state
        self.state_machine = state_machine

    async def __call__(self, client, event) -> bool:
        if isinstance(event, Object):
            user = event.author
        else:
            user = event
        if self.state_machine is None:
            return user.get_state() == self.state
        else:
            return self.state_machine[user.id] == self.state
