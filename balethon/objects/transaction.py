from . import Object


class Transaction(Object):

    def __init__(
            self,
            id: str = None,
            status: str = None,
            userID: int = None,
            amount: int = None,
            createdAt: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.status: str = status
        self.user_id: int = userID
        self.amount: int = amount
        self.created_at = createdAt
        
