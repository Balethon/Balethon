from . import Object


class PollOption(Object):
    @classmethod
    def from_protobuf(cls, protobuf_data):
        return cls(
            persistent_id=protobuf_data.id,
            text=protobuf_data.text
        )

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
