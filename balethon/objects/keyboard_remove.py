from . import Keyboard


class KeyboardRemove(Keyboard):

    def __init__(self):
        super().__init__([])

    def __repr__(self):
        return f"{type(self).__name__}()"
