from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExPeerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EX_PEER_TYPE_UNKNOWN: _ClassVar[ExPeerType]
    EX_PEER_TYPE_PRIVATE: _ClassVar[ExPeerType]
    EX_PEER_TYPE_GROUP: _ClassVar[ExPeerType]
    EX_PEER_TYPE_CHANNEL: _ClassVar[ExPeerType]
    EX_PEER_TYPE_BOT: _ClassVar[ExPeerType]
    EX_PEER_TYPE_SUPERGROUP: _ClassVar[ExPeerType]
    EX_PEER_TYPE_THREAD: _ClassVar[ExPeerType]

class Sex(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEX_UNKNOWN: _ClassVar[Sex]
    SEX_MALE: _ClassVar[Sex]
    SEX_FEMALE: _ClassVar[Sex]

class Restriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTRICTION_PRIVATE: _ClassVar[Restriction]
    RESTRICTION_PUBLIC: _ClassVar[Restriction]

class GroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROUP_TYPE_GROUP: _ClassVar[GroupType]
    GROUP_TYPE_CHANNEL: _ClassVar[GroupType]
    GROUP_TYPE_SUPER_GROUP: _ClassVar[GroupType]

class SendType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEND_TYPE_UNKNOWN: _ClassVar[SendType]
    SEND_TYPE_PHOTO: _ClassVar[SendType]
    SEND_TYPE_VIDEO: _ClassVar[SendType]
    SEND_TYPE_VOICE: _ClassVar[SendType]
    SEND_TYPE_GIF: _ClassVar[SendType]
    SEND_TYPE_AUDIO: _ClassVar[SendType]
    SEND_TYPE_DOCUMENT: _ClassVar[SendType]
    SEND_TYPE_STICKER: _ClassVar[SendType]
    SEND_TYPE_CROWDFUNDING: _ClassVar[SendType]
    SEND_TYPE_SPONSORED: _ClassVar[SendType]

class TypingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPING_TYPE_UNKNOWN: _ClassVar[TypingType]
    TYPING_TYPE_TEXT: _ClassVar[TypingType]
    TYPING_TYPE_VOICE_RECORDING: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_VOICE: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_FILE: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_PHOTO: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_VIDEO: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_MUSIC: _ClassVar[TypingType]
    TYPING_TYPE_CHOOSING_STICKER: _ClassVar[TypingType]
    TYPING_TYPE_CHOOSING_GIF: _ClassVar[TypingType]
    TYPING_TYPE_CREATING_GIFT_PACKET: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_ALBUM: _ClassVar[TypingType]
    TYPING_TYPE_CHOOSING_EMOJI: _ClassVar[TypingType]
EX_PEER_TYPE_UNKNOWN: ExPeerType
EX_PEER_TYPE_PRIVATE: ExPeerType
EX_PEER_TYPE_GROUP: ExPeerType
EX_PEER_TYPE_CHANNEL: ExPeerType
EX_PEER_TYPE_BOT: ExPeerType
EX_PEER_TYPE_SUPERGROUP: ExPeerType
EX_PEER_TYPE_THREAD: ExPeerType
SEX_UNKNOWN: Sex
SEX_MALE: Sex
SEX_FEMALE: Sex
RESTRICTION_PRIVATE: Restriction
RESTRICTION_PUBLIC: Restriction
GROUP_TYPE_GROUP: GroupType
GROUP_TYPE_CHANNEL: GroupType
GROUP_TYPE_SUPER_GROUP: GroupType
SEND_TYPE_UNKNOWN: SendType
SEND_TYPE_PHOTO: SendType
SEND_TYPE_VIDEO: SendType
SEND_TYPE_VOICE: SendType
SEND_TYPE_GIF: SendType
SEND_TYPE_AUDIO: SendType
SEND_TYPE_DOCUMENT: SendType
SEND_TYPE_STICKER: SendType
SEND_TYPE_CROWDFUNDING: SendType
SEND_TYPE_SPONSORED: SendType
TYPING_TYPE_UNKNOWN: TypingType
TYPING_TYPE_TEXT: TypingType
TYPING_TYPE_VOICE_RECORDING: TypingType
TYPING_TYPE_SENDING_VOICE: TypingType
TYPING_TYPE_SENDING_FILE: TypingType
TYPING_TYPE_SENDING_PHOTO: TypingType
TYPING_TYPE_SENDING_VIDEO: TypingType
TYPING_TYPE_SENDING_MUSIC: TypingType
TYPING_TYPE_CHOOSING_STICKER: TypingType
TYPING_TYPE_CHOOSING_GIF: TypingType
TYPING_TYPE_CREATING_GIFT_PACKET: TypingType
TYPING_TYPE_SENDING_ALBUM: TypingType
TYPING_TYPE_CHOOSING_EMOJI: TypingType

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

class DocumentExPhoto(_message.Message):
    __slots__ = ("w", "h")
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    w: int
    h: int
    def __init__(self, w: _Optional[int] = ..., h: _Optional[int] = ...) -> None: ...

class DocumentExVideo(_message.Message):
    __slots__ = ("w", "h", "duration")
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    w: int
    h: int
    duration: int
    def __init__(self, w: _Optional[int] = ..., h: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class DocumentExVoice(_message.Message):
    __slots__ = ("duration", "transcript")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    duration: int
    transcript: StringValue
    def __init__(self, duration: _Optional[int] = ..., transcript: _Optional[_Union[StringValue, _Mapping]] = ...) -> None: ...

class DocumentExGif(_message.Message):
    __slots__ = ("w", "h", "duration")
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    w: int
    h: int
    duration: int
    def __init__(self, w: _Optional[int] = ..., h: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class DocumentExAudio(_message.Message):
    __slots__ = ("duration", "album", "artist", "genre", "track", "cover")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ALBUM_FIELD_NUMBER: _ClassVar[int]
    ARTIST_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    COVER_FIELD_NUMBER: _ClassVar[int]
    duration: int
    album: str
    artist: str
    genre: str
    track: str
    cover: BytesValue
    def __init__(self, duration: _Optional[int] = ..., album: _Optional[str] = ..., artist: _Optional[str] = ..., genre: _Optional[str] = ..., track: _Optional[str] = ..., cover: _Optional[_Union[BytesValue, _Mapping]] = ...) -> None: ...

class DocumentEx(_message.Message):
    __slots__ = ("document_ex_photo", "document_ex_video", "document_ex_voice", "document_ex_gif", "document_ex_audio")
    DOCUMENT_EX_PHOTO_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_EX_VIDEO_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_EX_VOICE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_EX_GIF_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_EX_AUDIO_FIELD_NUMBER: _ClassVar[int]
    document_ex_photo: DocumentExPhoto
    document_ex_video: DocumentExVideo
    document_ex_voice: DocumentExVoice
    document_ex_gif: DocumentExGif
    document_ex_audio: DocumentExAudio
    def __init__(self, document_ex_photo: _Optional[_Union[DocumentExPhoto, _Mapping]] = ..., document_ex_video: _Optional[_Union[DocumentExVideo, _Mapping]] = ..., document_ex_voice: _Optional[_Union[DocumentExVoice, _Mapping]] = ..., document_ex_gif: _Optional[_Union[DocumentExGif, _Mapping]] = ..., document_ex_audio: _Optional[_Union[DocumentExAudio, _Mapping]] = ...) -> None: ...

class DocumentMessage(_message.Message):
    __slots__ = ("file_id", "access_hash", "file_size", "name", "mime_type", "thumb", "ext", "caption")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    THUMB_FIELD_NUMBER: _ClassVar[int]
    EXT_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    access_hash: int
    file_size: int
    name: str
    mime_type: str
    thumb: FastThumb
    ext: DocumentEx
    caption: TextMessage
    def __init__(self, file_id: _Optional[int] = ..., access_hash: _Optional[int] = ..., file_size: _Optional[int] = ..., name: _Optional[str] = ..., mime_type: _Optional[str] = ..., thumb: _Optional[_Union[FastThumb, _Mapping]] = ..., ext: _Optional[_Union[DocumentEx, _Mapping]] = ..., caption: _Optional[_Union[TextMessage, _Mapping]] = ...) -> None: ...

class TextMessage(_message.Message):
    __slots__ = ("text", "mentions")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    text: str
    mentions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, text: _Optional[str] = ..., mentions: _Optional[_Iterable[int]] = ...) -> None: ...

class JsonMessage(_message.Message):
    __slots__ = ("raw_json",)
    RAW_JSON_FIELD_NUMBER: _ClassVar[int]
    raw_json: str
    def __init__(self, raw_json: _Optional[str] = ...) -> None: ...

class ImageLocation(_message.Message):
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

class StickerMessage(_message.Message):
    __slots__ = ("sticker_id", "fast_preview", "image512", "image256", "sticker_collection_id", "sticker_collection_access_hash")
    STICKER_ID_FIELD_NUMBER: _ClassVar[int]
    FAST_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    IMAGE512_FIELD_NUMBER: _ClassVar[int]
    IMAGE256_FIELD_NUMBER: _ClassVar[int]
    STICKER_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    STICKER_COLLECTION_ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    sticker_id: Int32Value
    fast_preview: BytesValue
    image512: ImageLocation
    image256: ImageLocation
    sticker_collection_id: Int32Value
    sticker_collection_access_hash: Int64Value
    def __init__(self, sticker_id: _Optional[_Union[Int32Value, _Mapping]] = ..., fast_preview: _Optional[_Union[BytesValue, _Mapping]] = ..., image512: _Optional[_Union[ImageLocation, _Mapping]] = ..., image256: _Optional[_Union[ImageLocation, _Mapping]] = ..., sticker_collection_id: _Optional[_Union[Int32Value, _Mapping]] = ..., sticker_collection_access_hash: _Optional[_Union[Int64Value, _Mapping]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("document_message", "json_message", "sticker_message", "text_message")
    DOCUMENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    JSON_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STICKER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    document_message: DocumentMessage
    json_message: JsonMessage
    sticker_message: StickerMessage
    text_message: TextMessage
    def __init__(self, document_message: _Optional[_Union[DocumentMessage, _Mapping]] = ..., json_message: _Optional[_Union[JsonMessage, _Mapping]] = ..., sticker_message: _Optional[_Union[StickerMessage, _Mapping]] = ..., text_message: _Optional[_Union[TextMessage, _Mapping]] = ...) -> None: ...

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

class IntroPhoto(_message.Message):
    __slots__ = ("thumb", "width", "height")
    THUMB_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    thumb: FastThumb
    width: int
    height: int
    def __init__(self, thumb: _Optional[_Union[FastThumb, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class IntroGif(_message.Message):
    __slots__ = ("thumb", "width", "height")
    THUMB_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    thumb: FastThumb
    width: int
    height: int
    def __init__(self, thumb: _Optional[_Union[FastThumb, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class MediaExt(_message.Message):
    __slots__ = ("intro_gif", "intro_photo")
    INTRO_GIF_FIELD_NUMBER: _ClassVar[int]
    INTRO_PHOTO_FIELD_NUMBER: _ClassVar[int]
    intro_gif: IntroGif
    intro_photo: IntroPhoto
    def __init__(self, intro_gif: _Optional[_Union[IntroGif, _Mapping]] = ..., intro_photo: _Optional[_Union[IntroPhoto, _Mapping]] = ...) -> None: ...

class IntroMedia(_message.Message):
    __slots__ = ("file_location", "file_size", "mime_type", "file_name", "media_extra")
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MEDIA_EXTRA_FIELD_NUMBER: _ClassVar[int]
    file_location: FileLocation
    file_size: int
    mime_type: str
    file_name: str
    media_extra: MediaExt
    def __init__(self, file_location: _Optional[_Union[FileLocation, _Mapping]] = ..., file_size: _Optional[int] = ..., mime_type: _Optional[str] = ..., file_name: _Optional[str] = ..., media_extra: _Optional[_Union[MediaExt, _Mapping]] = ...) -> None: ...

class IntroMessage(_message.Message):
    __slots__ = ("text", "media")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    text: StringValue
    media: IntroMedia
    def __init__(self, text: _Optional[_Union[StringValue, _Mapping]] = ..., media: _Optional[_Union[IntroMedia, _Mapping]] = ...) -> None: ...

class Intro(_message.Message):
    __slots__ = ("text", "file_location", "width", "height", "file_size", "mime_type", "file_name", "thumb")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    THUMB_FIELD_NUMBER: _ClassVar[int]
    text: StringValue
    file_location: FileLocation
    width: int
    height: int
    file_size: int
    mime_type: str
    file_name: str
    thumb: FastThumb
    def __init__(self, text: _Optional[_Union[StringValue, _Mapping]] = ..., file_location: _Optional[_Union[FileLocation, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., file_size: _Optional[int] = ..., mime_type: _Optional[str] = ..., file_name: _Optional[str] = ..., thumb: _Optional[_Union[FastThumb, _Mapping]] = ...) -> None: ...

class BotExInfo(_message.Message):
    __slots__ = ("bot_active_users", "has_main_mini_app", "intro", "intro_message", "has_timche_profile")
    BOT_ACTIVE_USERS_FIELD_NUMBER: _ClassVar[int]
    HAS_MAIN_MINI_APP_FIELD_NUMBER: _ClassVar[int]
    INTRO_FIELD_NUMBER: _ClassVar[int]
    INTRO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HAS_TIMCHE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    bot_active_users: StringValue
    has_main_mini_app: BoolValue
    intro: Intro
    intro_message: IntroMessage
    has_timche_profile: BoolValue
    def __init__(self, bot_active_users: _Optional[_Union[StringValue, _Mapping]] = ..., has_main_mini_app: _Optional[_Union[BoolValue, _Mapping]] = ..., intro: _Optional[_Union[Intro, _Mapping]] = ..., intro_message: _Optional[_Union[IntroMessage, _Mapping]] = ..., has_timche_profile: _Optional[_Union[BoolValue, _Mapping]] = ...) -> None: ...

class ExInfo(_message.Message):
    __slots__ = ("ex_peer_type",)
    EX_PEER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ex_peer_type: ExPeerType
    def __init__(self, ex_peer_type: _Optional[_Union[ExPeerType, str]] = ...) -> None: ...

class Int64Value(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class BoolValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class FileLocation(_message.Message):
    __slots__ = ("file_id", "access_hash", "file_storage_version")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    FILE_STORAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    access_hash: int
    file_storage_version: Int32Value
    def __init__(self, file_id: _Optional[int] = ..., access_hash: _Optional[int] = ..., file_storage_version: _Optional[_Union[Int32Value, _Mapping]] = ...) -> None: ...

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
    id: Int64Value
    date: Int64Value
    def __init__(self, small_image: _Optional[_Union[AvatarImage, _Mapping]] = ..., large_image: _Optional[_Union[AvatarImage, _Mapping]] = ..., full_image: _Optional[_Union[AvatarImage, _Mapping]] = ..., id: _Optional[_Union[Int64Value, _Mapping]] = ..., date: _Optional[_Union[Int64Value, _Mapping]] = ...) -> None: ...

class StringValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class BytesValue(_message.Message):
    __slots__ = ("Value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Value: str
    def __init__(self, Value: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "access_hash", "name", "local_name", "sex", "avatar", "is_bot", "nick", "is_deleted", "created_at", "ex_info", "bot_ex_info")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_NAME_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    IS_BOT_FIELD_NUMBER: _ClassVar[int]
    NICK_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EX_INFO_FIELD_NUMBER: _ClassVar[int]
    BOT_EX_INFO_FIELD_NUMBER: _ClassVar[int]
    id: int
    access_hash: int
    name: str
    local_name: StringValue
    sex: Sex
    avatar: Avatar
    is_bot: BoolValue
    nick: StringValue
    is_deleted: BoolValue
    created_at: Int64Value
    ex_info: ExInfo
    bot_ex_info: BotExInfo
    def __init__(self, id: _Optional[int] = ..., access_hash: _Optional[int] = ..., name: _Optional[str] = ..., local_name: _Optional[_Union[StringValue, _Mapping]] = ..., sex: _Optional[_Union[Sex, str]] = ..., avatar: _Optional[_Union[Avatar, _Mapping]] = ..., is_bot: _Optional[_Union[BoolValue, _Mapping]] = ..., nick: _Optional[_Union[StringValue, _Mapping]] = ..., is_deleted: _Optional[_Union[BoolValue, _Mapping]] = ..., created_at: _Optional[_Union[Int64Value, _Mapping]] = ..., ex_info: _Optional[_Union[ExInfo, _Mapping]] = ..., bot_ex_info: _Optional[_Union[BotExInfo, _Mapping]] = ...) -> None: ...

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

class Int32Value(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class FullGroup(_message.Message):
    __slots__ = ("id", "title", "avatar", "owner_uid", "create_date", "group_type", "is_member", "members_count", "nick", "permissions", "default_permissions", "theme", "about", "members", "ex_info", "pin", "restriction", "available_reactions", "is_suspend", "linked_group_peer_id", "discussion_group_enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    OWNER_UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_MEMBER_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    NICK_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    EX_INFO_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_REACTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_SUSPEND_FIELD_NUMBER: _ClassVar[int]
    LINKED_GROUP_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    DISCUSSION_GROUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    avatar: Avatar
    owner_uid: int
    create_date: int
    group_type: GroupType
    is_member: BoolValue
    members_count: Int32Value
    nick: StringValue
    permissions: Permissions
    default_permissions: Permissions
    theme: StringValue
    about: StringValue
    members: _containers.RepeatedCompositeFieldContainer[Member]
    ex_info: ExInfo
    pin: MessageContainer
    restriction: Restriction
    available_reactions: _containers.RepeatedScalarFieldContainer[str]
    is_suspend: BoolValue
    linked_group_peer_id: Int32Value
    discussion_group_enabled: BoolValue
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., avatar: _Optional[_Union[Avatar, _Mapping]] = ..., owner_uid: _Optional[int] = ..., create_date: _Optional[int] = ..., group_type: _Optional[_Union[GroupType, str]] = ..., is_member: _Optional[_Union[BoolValue, _Mapping]] = ..., members_count: _Optional[_Union[Int32Value, _Mapping]] = ..., nick: _Optional[_Union[StringValue, _Mapping]] = ..., permissions: _Optional[_Union[Permissions, _Mapping]] = ..., default_permissions: _Optional[_Union[Permissions, _Mapping]] = ..., theme: _Optional[_Union[StringValue, _Mapping]] = ..., about: _Optional[_Union[StringValue, _Mapping]] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., ex_info: _Optional[_Union[ExInfo, _Mapping]] = ..., pin: _Optional[_Union[MessageContainer, _Mapping]] = ..., restriction: _Optional[_Union[Restriction, str]] = ..., available_reactions: _Optional[_Iterable[str]] = ..., is_suspend: _Optional[_Union[BoolValue, _Mapping]] = ..., linked_group_peer_id: _Optional[_Union[Int32Value, _Mapping]] = ..., discussion_group_enabled: _Optional[_Union[BoolValue, _Mapping]] = ...) -> None: ...

class MessagesViews(_message.Message):
    __slots__ = ("mid", "views")
    MID_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    mid: MessageId
    views: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, mid: _Optional[_Union[MessageId, _Mapping]] = ..., views: _Optional[_Iterable[int]] = ...) -> None: ...

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
    is_admin: BoolValue
    promoter_user_id: int
    promoted_at: int
    permissions: Permissions
    title: str
    def __init__(self, uid: _Optional[int] = ..., inviter_uid: _Optional[int] = ..., date: _Optional[int] = ..., is_admin: _Optional[_Union[BoolValue, _Mapping]] = ..., promoter_user_id: _Optional[int] = ..., promoted_at: _Optional[int] = ..., permissions: _Optional[_Union[Permissions, _Mapping]] = ..., title: _Optional[str] = ...) -> None: ...

class SendTypeValue(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: SendType
    def __init__(self, type: _Optional[_Union[SendType, str]] = ...) -> None: ...

class Avatars(_message.Message):
    __slots__ = ("avatars",)
    AVATARS_FIELD_NUMBER: _ClassVar[int]
    avatars: _containers.RepeatedCompositeFieldContainer[Avatar]
    def __init__(self, avatars: _Optional[_Iterable[_Union[Avatar, _Mapping]]] = ...) -> None: ...

class FileUrlDescription(_message.Message):
    __slots__ = ("file_id", "url", "timeout", "unsigned_url", "chunk_size")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    UNSIGNED_URL_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    url: str
    timeout: int
    unsigned_url: str
    chunk_size: Int32Value
    def __init__(self, file_id: _Optional[int] = ..., url: _Optional[str] = ..., timeout: _Optional[int] = ..., unsigned_url: _Optional[str] = ..., chunk_size: _Optional[_Union[Int32Value, _Mapping]] = ...) -> None: ...

class SingleMedia(_message.Message):
    __slots__ = ("random_id", "media")
    RANDOM_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    random_id: int
    media: DocumentMessage
    def __init__(self, random_id: _Optional[int] = ..., media: _Optional[_Union[DocumentMessage, _Mapping]] = ...) -> None: ...
