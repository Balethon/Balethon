from . import Object


class ForumTopic(Object):

    def __init__(
            self,
            message_thread_id: int,
            name: str,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.message_thread_id: int = message_thread_id
        self.name: str = name
