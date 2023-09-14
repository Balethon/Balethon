from . import Object
import balethon


class Error(Object):
    attribute_names = [
        ("code", "error_code")
    ]

    def __init__(
            self,
            client: "balethon.Client" = None,
            code: int = None,
            ok: bool = None,
            description: str = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.code: int = code
        self.ok: bool = ok
        self.description: str = description
