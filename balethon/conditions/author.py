from .condition import Condition


class Author(Condition):
    def __init__(self, *authors):
        super().__init__()
        self.authors = set(authors)

    async def __call__(self, client, event) -> bool:
        from ..objects import Object
        if isinstance(event, Object):
            event = event.author.id
        return event in self.authors
