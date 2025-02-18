from . import Object


class WebAppInfo(Object):
    def __init__(
            self,
            url: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.url: str = url
