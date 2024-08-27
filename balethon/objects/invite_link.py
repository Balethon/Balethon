from . import Object
from balethon import objects


class InviteLink(Object):
    attribute_names = [
        ("link", "invite_link")
    ]

    def __init__(
            self,
            link: str = None,
            creator: "objects.User" = None,
            creates_join_request: bool = None,
            is_primary: bool = None,
            is_revoked: bool = None,
            name: str = None,
            expire_date: int = None,
            member_limit: int = None,
            pending_join_request_count: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.link: str = link
        self.creator: "objects.User" = creator
        self.creates_join_request: bool = creates_join_request
        self.is_primary: bool = is_primary
        self.is_revoked: bool = is_revoked
        self.name: str = name
        self.expire_date: int = expire_date
        self.member_limit: int = member_limit
        self.pending_join_request_count: int = pending_join_request_count
