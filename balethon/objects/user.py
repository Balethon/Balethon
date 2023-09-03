from . import Object
import balethon


class User(Object):

    def __init__(
            self,
            client: "balethon.Client" = None,
            id: int = None,
            username: str = None,
            first_name: str = None,
            last_name: str = None,
            language_code: str = None,
            is_bot: bool = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.id: int = id
        self.username: str = username
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.language_code: str = language_code
        self.is_bot: bool = is_bot

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.first_name:
            return self.first_name
        return ""
