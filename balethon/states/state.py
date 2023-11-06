class State:

    def __init__(self, name=None, *, previous=None, next=None, group=None):
        self.name = name
        self.previous = previous
        self.next = next
        self.group = group

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.group.__name__}.{self.name}"
