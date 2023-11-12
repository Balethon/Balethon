class State:

    def __init__(self, name=None, group=None):
        self.name = name
        self.group = group

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.group.__name__}.{self.name}"
