from ..object import Object


class Location(Object):

    def __init__(self, longitude, latitude, **kwargs):
        super().__init__()
        self.longitude = longitude
        self.latitude = latitude
