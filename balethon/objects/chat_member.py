from . import Object
from balethon import objects


class ChatMember(Object):

    def __init__(
            self,
            is_member: bool = None,
            can_send_media: bool = None,
            can_send_gif_stickers: bool = None,
            can_forward_message_from: bool = None,
            can_send_gift_packet: bool = None,
            can_send_link_message: bool = None,
            can_send_forwarded_message: bool = None,
            can_kick_user: bool = None,
            can_send_message: bool = None,
            can_see_members: bool = None,
            can_add_story: bool = None,
            user: "objects.User" = None,
            status: str = None,
            can_change_info: bool = None,
            can_delete_messages: bool = None,
            can_invite_users: bool = None,
            can_restrict_members: bool = None,
            can_pin_messages: bool = None,
            can_promote_members: bool = None,
            can_send_messages: bool = None,
            can_send_media_messages: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.is_member: bool = is_member
        self.can_send_media: bool = can_send_media
        self.can_send_gif_stickers: bool = can_send_gif_stickers
        self.can_forward_message_from: bool = can_forward_message_from
        self.can_send_gift_packet: bool = can_send_gift_packet
        self.can_send_link_message: bool = can_send_link_message
        self.can_send_forwarded_message: bool = can_send_forwarded_message
        self.can_kick_user: bool = can_kick_user
        self.can_send_message: bool = can_send_message
        self.can_see_members: bool = can_see_members
        self.can_add_story: bool = can_add_story
        self.user: "objects.User" = user
        self.status: str = status
        self.can_change_info: bool = can_change_info
        self.can_delete_messages: bool = can_delete_messages
        self.can_invite_users: bool = can_invite_users
        self.can_restrict_members: bool = can_restrict_members
        self.can_pin_messages: bool = can_pin_messages
        self.can_promote_members: bool = can_promote_members
        self.can_send_messages: bool = can_send_messages
        self.can_send_media_messages: bool = can_send_media_messages
