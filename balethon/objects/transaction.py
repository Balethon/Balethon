from . import Object


class Transaction(Object):
    attribute_names = [
        ("user_id", "userID"),
        ("created_at", "createdAt"),
    ]

    def __init__(
            self,
            id: str = None,
            status: str = None,
            user_id: int = None,
            amount: int = None,
            created_at: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.status: str = status
        self.user_id: int = user_id
        self.amount: int = amount
        self.created_at: int = created_at
