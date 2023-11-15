class State:

    def __init__(self):
        self.name = None
        self.group = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.group.__name__}.{self.name}"
