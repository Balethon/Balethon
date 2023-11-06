from . import State


class StateGroup:

    def __init_subclass__(cls, **kwargs):
        for name, value in cls.__dict__.items():
            if isinstance(value, State):
                if value.name is None:
                    value.name = name
                value.group = cls
                if isinstance(value.previous, str):
                    value.previous = getattr(value.group, value.previous)
                if isinstance(value.next, str):
                    value.next = getattr(value.group, value.next)
