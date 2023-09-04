from . import Object
import balethon
from balethon import objects


class ChatMember(Object):

    def __init__(
            self,
            client: "balethon.Client" = None,
            user: "objects.User" = None,
            status: str = None,
            until_date: "objects.Date" = None,
            can_be_edited: bool = None,
            can_change_info: bool = None,
            can_post_messages: bool = None,
            can_edit_messages: bool = None,
            can_delete_messages: bool = None,
            can_invite_users: bool = None,
            can_restrict_members: bool = None,
            can_pin_messages: bool = None,
            can_promote_members: bool = None,
            can_send_messages: bool = None,
            can_send_media_messages: bool = None,
            can_send_other_messages: bool = None,
            can_add_web_page_previews: bool = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.user: "objects.User" = user
        self.status: str = status
        self.until_date: "objects.Date" = until_date
        self.can_be_edited: bool = can_be_edited
        self.can_change_info: bool = can_change_info
        self.can_post_messages: bool = can_post_messages
        self.can_edit_messages: bool = can_edit_messages
        self.can_delete_messages: bool = can_delete_messages
        self.can_invite_users: bool = can_invite_users
        self.can_restrict_members: bool = can_restrict_members
        self.can_pin_messages: bool = can_pin_messages
        self.can_promote_members: bool = can_promote_members
        self.can_send_messages: bool = can_send_messages
        self.can_send_media_messages: bool = can_send_media_messages
        self.can_send_other_messages: bool = can_send_other_messages
        self.can_add_web_page_previews: bool = can_add_web_page_previews
