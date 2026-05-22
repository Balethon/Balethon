from . import Object


class PollOption(Object):

    def __init__(
            self,
            persistent_id: str = None,
            text: str = None,
            voter_count: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.persistent_id: str = persistent_id
        self.text: str = text
        self.voter_count: int = voter_count
