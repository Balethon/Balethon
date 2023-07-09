from ..object import Object

class User(Object):
    
    @classmethod
    def from_dict(cls, user_dict: dict):
        return cls(**user_dict)
    
    def __init__(
            self,
            id: int,
            username: str = None,
            first_name: str = None,
            last_name: str = None,
            language_code: str = None,
            is_bot: bool = None,
    ):
        super().__init__()
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.language_code = language_code
        self.is_bot = is_bot
