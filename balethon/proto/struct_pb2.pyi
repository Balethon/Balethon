from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Peer(_message.Message):
    __slots__ = ("type", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class ExPeer(_message.Message):
    __slots__ = ("type", "id", "access_hash")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    access_hash: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., access_hash: _Optional[int] = ...) -> None: ...

class FastThumb(_message.Message):
    __slots__ = ("w", "h", "thumb")
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    THUMB_FIELD_NUMBER: _ClassVar[int]
    w: int
    h: int
    thumb: bytes
    def __init__(self, w: _Optional[int] = ..., h: _Optional[int] = ..., thumb: _Optional[bytes] = ...) -> None: ...

class DocumentMessage(_message.Message):
    __slots__ = ("file_id", "access_hash", "file_size", "name", "mime_type", "thumb", "caption")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    THUMB_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    access_hash: int
    file_size: int
    name: str
    mime_type: str
    thumb: FastThumb
    caption: TextMessage
    def __init__(self, file_id: _Optional[int] = ..., access_hash: _Optional[int] = ..., file_size: _Optional[int] = ..., name: _Optional[str] = ..., mime_type: _Optional[str] = ..., thumb: _Optional[_Union[FastThumb, _Mapping]] = ..., caption: _Optional[_Union[TextMessage, _Mapping]] = ...) -> None: ...

class TextMessage(_message.Message):
    __slots__ = ("text", "mentions")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    text: str
    mentions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, text: _Optional[str] = ..., mentions: _Optional[_Iterable[int]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("document_message", "text_message")
    DOCUMENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    document_message: DocumentMessage
    text_message: TextMessage
    def __init__(self, document_message: _Optional[_Union[DocumentMessage, _Mapping]] = ..., text_message: _Optional[_Union[TextMessage, _Mapping]] = ...) -> None: ...

class DeleteDates(_message.Message):
    __slots__ = ("dates",)
    DATES_FIELD_NUMBER: _ClassVar[int]
    dates: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, dates: _Optional[_Iterable[int]] = ...) -> None: ...

class MessageId(_message.Message):
    __slots__ = ("date", "rid", "seq")
    DATE_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    date: int
    rid: int
    seq: int
    def __init__(self, date: _Optional[int] = ..., rid: _Optional[int] = ..., seq: _Optional[int] = ...) -> None: ...

class OutPeer(_message.Message):
    __slots__ = ("type", "id", "access_hash")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    access_hash: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., access_hash: _Optional[int] = ...) -> None: ...

class GroupOutPeer(_message.Message):
    __slots__ = ("group_id", "access_hash")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    access_hash: int
    def __init__(self, group_id: _Optional[int] = ..., access_hash: _Optional[int] = ...) -> None: ...

class UserOutPeer(_message.Message):
    __slots__ = ("uid", "access_hash")
    UID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    uid: int
    access_hash: int
    def __init__(self, uid: _Optional[int] = ..., access_hash: _Optional[int] = ...) -> None: ...

class QuotedMessage(_message.Message):
    __slots__ = ("message_id", "sender_user_id", "message_date", "quoted_message_content", "quoted_peer")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_DATE_FIELD_NUMBER: _ClassVar[int]
    QUOTED_MESSAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    QUOTED_PEER_FIELD_NUMBER: _ClassVar[int]
    message_id: Int64Value
    sender_user_id: int
    message_date: int
    quoted_message_content: Message
    quoted_peer: OutPeer
    def __init__(self, message_id: _Optional[_Union[Int64Value, _Mapping]] = ..., sender_user_id: _Optional[int] = ..., message_date: _Optional[int] = ..., quoted_message_content: _Optional[_Union[Message, _Mapping]] = ..., quoted_peer: _Optional[_Union[OutPeer, _Mapping]] = ...) -> None: ...

class MessageContainer(_message.Message):
    __slots__ = ("sender_uid", "rid", "date", "message", "quoted_message")
    SENDER_UID_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    QUOTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sender_uid: int
    rid: int
    date: int
    message: Message
    quoted_message: QuotedMessage
    def __init__(self, sender_uid: _Optional[int] = ..., rid: _Optional[int] = ..., date: _Optional[int] = ..., message: _Optional[_Union[Message, _Mapping]] = ..., quoted_message: _Optional[_Union[QuotedMessage, _Mapping]] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("id", "title", "members_count", "available_reactions")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_REACTIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    members_count: int
    available_reactions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., members_count: _Optional[int] = ..., available_reactions: _Optional[_Iterable[str]] = ...) -> None: ...

class FullGroup(_message.Message):
    __slots__ = ("id", "title", "members_count", "available_reactions")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_REACTIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    members_count: int
    available_reactions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., members_count: _Optional[int] = ..., available_reactions: _Optional[_Iterable[str]] = ...) -> None: ...

class MessagesViews(_message.Message):
    __slots__ = ("mid", "views")
    MID_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    mid: MessageId
    views: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, mid: _Optional[_Union[MessageId, _Mapping]] = ..., views: _Optional[_Iterable[int]] = ...) -> None: ...

class Avatar(_message.Message):
    __slots__ = ("small_image", "large_image", "full_image", "id", "date")
    SMALL_IMAGE_FIELD_NUMBER: _ClassVar[int]
    LARGE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    FULL_IMAGE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    small_image: AvatarImage
    large_image: AvatarImage
    full_image: AvatarImage
    id: int
    date: int
    def __init__(self, small_image: _Optional[_Union[AvatarImage, _Mapping]] = ..., large_image: _Optional[_Union[AvatarImage, _Mapping]] = ..., full_image: _Optional[_Union[AvatarImage, _Mapping]] = ..., id: _Optional[int] = ..., date: _Optional[int] = ...) -> None: ...

class AvatarImage(_message.Message):
    __slots__ = ("file_location", "width", "height", "file_size")
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_location: FileLocation
    width: int
    height: int
    file_size: int
    def __init__(self, file_location: _Optional[_Union[FileLocation, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., file_size: _Optional[int] = ...) -> None: ...

class FileLocation(_message.Message):
    __slots__ = ("file_id", "access_hash", "file_storage_version")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    FILE_STORAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    access_hash: int
    file_storage_version: int
    def __init__(self, file_id: _Optional[int] = ..., access_hash: _Optional[int] = ..., file_storage_version: _Optional[int] = ...) -> None: ...

class Int64Value(_message.Message):
    __slots__ = ("date",)
    DATE_FIELD_NUMBER: _ClassVar[int]
    date: int
    def __init__(self, date: _Optional[int] = ...) -> None: ...

class HistoryMessageIdentifier(_message.Message):
    __slots__ = ("peer", "random_id", "date")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RANDOM_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    peer: Peer
    random_id: int
    date: Int64Value
    def __init__(self, peer: _Optional[_Union[Peer, _Mapping]] = ..., random_id: _Optional[int] = ..., date: _Optional[_Union[Int64Value, _Mapping]] = ...) -> None: ...

class Permissions(_message.Message):
    __slots__ = ("see_message", "delete_message", "kick_user", "pin_message", "invite_user", "add_admin", "change_info", "send_message", "see_members", "edit_message", "send_media", "send_gif_stickers", "reply_to_story", "forward_message_from", "send_gift_packet", "start_call", "send_link_message", "send_forwarded_message", "add_story", "manage_call")
    SEE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KICK_USER_FIELD_NUMBER: _ClassVar[int]
    PIN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INVITE_USER_FIELD_NUMBER: _ClassVar[int]
    ADD_ADMIN_FIELD_NUMBER: _ClassVar[int]
    CHANGE_INFO_FIELD_NUMBER: _ClassVar[int]
    SEND_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    EDIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEND_MEDIA_FIELD_NUMBER: _ClassVar[int]
    SEND_GIF_STICKERS_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_STORY_FIELD_NUMBER: _ClassVar[int]
    FORWARD_MESSAGE_FROM_FIELD_NUMBER: _ClassVar[int]
    SEND_GIFT_PACKET_FIELD_NUMBER: _ClassVar[int]
    START_CALL_FIELD_NUMBER: _ClassVar[int]
    SEND_LINK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEND_FORWARDED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADD_STORY_FIELD_NUMBER: _ClassVar[int]
    MANAGE_CALL_FIELD_NUMBER: _ClassVar[int]
    see_message: bool
    delete_message: bool
    kick_user: bool
    pin_message: bool
    invite_user: bool
    add_admin: bool
    change_info: bool
    send_message: bool
    see_members: bool
    edit_message: bool
    send_media: bool
    send_gif_stickers: bool
    reply_to_story: bool
    forward_message_from: bool
    send_gift_packet: bool
    start_call: bool
    send_link_message: bool
    send_forwarded_message: bool
    add_story: bool
    manage_call: bool
    def __init__(self, see_message: bool = ..., delete_message: bool = ..., kick_user: bool = ..., pin_message: bool = ..., invite_user: bool = ..., add_admin: bool = ..., change_info: bool = ..., send_message: bool = ..., see_members: bool = ..., edit_message: bool = ..., send_media: bool = ..., send_gif_stickers: bool = ..., reply_to_story: bool = ..., forward_message_from: bool = ..., send_gift_packet: bool = ..., start_call: bool = ..., send_link_message: bool = ..., send_forwarded_message: bool = ..., add_story: bool = ..., manage_call: bool = ...) -> None: ...

class LoadMembersCondition(_message.Message):
    __slots__ = ("excepted_permissions", "contacts", "query")
    EXCEPTED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    excepted_permissions: bool
    contacts: bool
    query: str
    def __init__(self, excepted_permissions: bool = ..., contacts: bool = ..., query: _Optional[str] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ("uid", "inviter_uid", "date", "is_admin", "promoter_user_id", "promoted_at", "permissions", "title")
    UID_FIELD_NUMBER: _ClassVar[int]
    INVITER_UID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    PROMOTER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROMOTED_AT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    uid: int
    inviter_uid: int
    date: int
    is_admin: bool
    promoter_user_id: int
    promoted_at: int
    permissions: Permissions
    title: str
    def __init__(self, uid: _Optional[int] = ..., inviter_uid: _Optional[int] = ..., date: _Optional[int] = ..., is_admin: bool = ..., promoter_user_id: _Optional[int] = ..., promoted_at: _Optional[int] = ..., permissions: _Optional[_Union[Permissions, _Mapping]] = ..., title: _Optional[str] = ...) -> None: ...
