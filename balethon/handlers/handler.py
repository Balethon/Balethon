class Handler:

    def __init__(self, callback, condition=None):
        self.callback = callback
        self.condition = condition
