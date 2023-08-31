from ..object import Object


class User(Object):
    id: int
    username: str
    first_name: str
    last_name: str
    language_code: str
    is_bot: bool

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.first_name:
            return self.first_name
        return ""
