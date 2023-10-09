from . import Object


class Contact(Object):

    def __init__(
            self,
            phone_number: str = None,
            first_name: str = None,
            last_name: str = None,
            user_id: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.phone_number: str = phone_number
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.user_id: int = user_id
