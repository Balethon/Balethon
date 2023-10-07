from . import Object


class LabeledPrice(Object):

    def __init__(
            self,
            label: str = None,
            amount: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.label: str = label
        self.amount: int = amount
