from . import State


class StateGroup:

    def __init_subclass__(cls, **kwargs):
        for name, state in cls.__dict__.items():
            if isinstance(state, State):
                if state.name is None:
                    state.name = name
                state.group = cls
