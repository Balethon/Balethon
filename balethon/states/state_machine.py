class StateMachine:

    def __init__(self, state_group):
        self.state_group = state_group
        self.states = {}

    def set_state(self, user_id, state=None):
        self.states[user_id] = state

    def get_state(self, user_id):
        try:
            return self.states[user_id]
        except KeyError:
            return None

    def on(self, state):
        async def condition(client, update):
            return self.get_state(update.author.id) == state
        return condition
