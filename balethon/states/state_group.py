from . import State


class StateGroup:

    @classmethod
    def get_state_dict(cls):
        return {name: state for name, state in cls.__dict__.items() if isinstance(state, State)}

    def __init_subclass__(cls, **kwargs):
        for name, state in cls.get_state_dict().items():
            state.name = name
            state.group = cls
