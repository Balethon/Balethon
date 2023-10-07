from .object import Object


class ShippingAddress(Object):

    def __init__(
            self,
            country_code: str = None,
            stat: str = None,
            city: str = None,
            street_line1: str = None,
            street_line2: str = None,
            post_code: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.country_code: str = country_code
        self.stat: str = stat
        self.city: str = city
        self.street_line1: str = street_line1
        self.street_line2: str = street_line2
        self.post_code: str = post_code
