from ..conditions import Condition


class StateMachine:

    def __init__(self):
        self.states = {}

    def __setitem__(self, user_id, state):
        self.states[user_id] = state

    def __getitem__(self, user_id):
        try:
            return self.states[user_id]
        except KeyError:
            return None

    def __delitem__(self, user_id):
        del self.states[user_id]

    def at(self, state):
        @Condition.create
        async def at_state(client, update):
            return self[update.author.id] == state
        return at_state
