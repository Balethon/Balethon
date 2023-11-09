from ..conditions import Condition


class StateMachine:

    def __init__(self, state_group):
        self.state_group = state_group
        self.states = {}

    def set_state(self, user_id, state):
        self.states[user_id] = state

    def get_state(self, user_id):
        try:
            return self.states[user_id]
        except KeyError:
            return None

    def go_to_next_state(self, user_id):
        current_state = self.get_state(user_id)
        self.set_state(user_id, current_state.next)

    def go_to_previous_state(self, user_id):
        current_state = self.get_state(user_id)
        self.set_state(user_id, current_state.previous)

    def at(self, state):
        @Condition.create
        async def condition(client, update):
            return self.get_state(update.author.id) == state
        return condition
