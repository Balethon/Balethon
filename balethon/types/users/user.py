from ..object import Object


class User(Object):

    def __init__(
            self,
            id=None,
            username=None,
            first_name=None,
            last_name=None,
            language_code=None,
            is_bot=None,
            client=None,
            **kwargs
    ):
        super().__init__(client)
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.language_code = language_code
        self.is_bot = is_bot
