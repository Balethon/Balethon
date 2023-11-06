class StateGroup:

    def __init_subclass__(cls, **kwargs):
        for name, value in cls.__dict__.items():
            value.name = name
