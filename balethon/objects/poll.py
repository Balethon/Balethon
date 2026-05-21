from typing import List

from balethon import enums
from . import Object
from .poll_option import PollOption


class Poll(Object):

    def __init__(
            self,
            id: str = None,
            question: str = None,
            options: List[PollOption] = None,
            total_voter_count: int = None,
            is_closed: bool = None,
            is_anonymous: bool = None,
            type: "enums.PollType" = None,
            allows_multiple_answers: bool = None,
            allows_revoting: bool = None,
            members_only: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.question: str = question
        self.options: List[PollOption] = options
        self.total_voter_count: int = total_voter_count
        self.is_closed: bool = is_closed
        self.is_anonymous: bool = is_anonymous
        self.type: "enums.PollType" = type
        self.allows_multiple_answers: bool = allows_multiple_answers
        self.allows_revoting: bool = allows_revoting
        self.members_only: bool = members_only
