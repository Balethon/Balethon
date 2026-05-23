from . import Object


class ChatPermissions(Object):

    def __init__(
            self,
            can_send_messages: bool = None,
            can_send_audios: bool = None,
            can_send_documents: bool = None,
            can_send_photos: bool = None,
            can_send_videos: bool = None,
            can_change_info: bool = None,
            can_invite_users: bool = None,
            can_pin_messages: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.can_send_messages: bool = can_send_messages
        self.can_send_audios: bool = can_send_audios
        self.can_send_documents: bool = can_send_documents
        self.can_send_photos: bool = can_send_photos
        self.can_send_videos: bool = can_send_videos
        self.can_change_info: bool = can_change_info
        self.can_invite_users: bool = can_invite_users
        self.can_pin_messages: bool = can_pin_messages
