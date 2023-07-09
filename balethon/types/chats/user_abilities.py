from ..object import Object

class UserAbilities(Object):
    
    @classmethod
    def from_dict(cls, chat_dict: dict):
        chat_dict.pop("user")
        
        return cls(**chat_dict)
    
    def __init__(
            self,
            status: str = None,
            untli_date: int = None,
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
            can_add_web_page_previews: bool = None
    ):
        super().__init__()
        self.status = status
        self.untli_date = untli_date
        self.can_be_edited = can_be_edited
        self.can_change_info = can_change_info
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_delete_messages = can_delete_messages
        self.can_invite_users = can_invite_users
        self.can_restrict_members = can_restrict_members
        self.can_pin_messages = can_pin_messages
        self.can_promote_members = can_promote_members
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews

