from ..object import Object


class Chat(Object):

    def __init__(
            self,
            id=None,
            type=None,
            title=None,
            username=None,
            first_name=None,
            last_name=None,
            all_members_are_administrators=None,
            description=None,
            invite_link=None,
            pinned_message=None,
            sticker_set_name=None,
            can_set_sticker_set=None,
            client=None,
            **kwargs
    ):
        super().__init__(client)
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.all_members_are_administrators = all_members_are_administrators
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
