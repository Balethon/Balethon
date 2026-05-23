from . import Object


class Location(Object):

    def __init__(
            self,
            longitude: float = None,
            latitude: float = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.longitude: float = longitude
        self.latitude: float = latitude
