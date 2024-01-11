from .condition import Condition


class Author(Condition):

    def __init__(self, *authors):
        super().__init__()
        self.authors = authors

    async def __call__(self, client, update) -> bool:
        from ..objects import Object
        if isinstance(update, Object):
            update = update.author.id
        return update in self.authors
