class Entities:

    def __init__(
            self,
            type=None,
            offset=None,
            length=None,
            url=None,
            user=None
    ):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        super().__init__()
