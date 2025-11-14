from . import Object


class WebAppData(Object):

    def __init__(
            self,
            data: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.data: str = data
