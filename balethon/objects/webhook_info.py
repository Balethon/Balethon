from . import Object


class WebhookInfo(Object):

    def __init__(
            self,
            url: str,
            has_custom_certificate: bool,
            pending_update_count: int,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.url: str = url
        self.has_custom_certificate: bool = has_custom_certificate
        self.pending_update_count: int = pending_update_count
