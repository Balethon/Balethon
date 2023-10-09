from . import Object


class Location(Object):

    def __init__(
            self,
            longitude: int = None,
            latitude: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.longitude: int = longitude
        self.latitude: int = latitude
