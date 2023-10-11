from . import Object


class Invoice(Object):

    def __init__(
            self,
            title: str = None,
            description: str = None,
            start_parameter: str = None,
            currency: str = None,
            total_amount: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.title: str = title
        self.description: str = description
        self.start_parameter: str = start_parameter
        self.currency: str = currency
        self.total_amount: int = total_amount
