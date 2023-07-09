from ..object import Object


class Contact(Object):

    def __init__(
            self,
            phone_number=None,
            first_name=None,
            last_name=None,
            user_id=None,
            **kwargs
    ):
        super().__init__()
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
