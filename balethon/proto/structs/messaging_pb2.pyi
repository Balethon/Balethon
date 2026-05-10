from ..structs import collections_pb2 as _collections_pb2
from ..structs import files_pb2 as _files_pb2
from ..structs import peers_pb2 as _peers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
    transcript: _collections_pb2.StringValue
    def __init__(self, duration: _Optional[int] = ..., transcript: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ...) -> None: ...

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
    cover: _collections_pb2.BytesValue
    def __init__(self, duration: _Optional[int] = ..., album: _Optional[str] = ..., artist: _Optional[str] = ..., genre: _Optional[str] = ..., track: _Optional[str] = ..., cover: _Optional[_Union[_collections_pb2.BytesValue, _Mapping]] = ...) -> None: ...

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
    thumb: _files_pb2.FastThumb
    ext: DocumentEx
    caption: TextMessage
    def __init__(self, file_id: _Optional[int] = ..., access_hash: _Optional[int] = ..., file_size: _Optional[int] = ..., name: _Optional[str] = ..., mime_type: _Optional[str] = ..., thumb: _Optional[_Union[_files_pb2.FastThumb, _Mapping]] = ..., ext: _Optional[_Union[DocumentEx, _Mapping]] = ..., caption: _Optional[_Union[TextMessage, _Mapping]] = ...) -> None: ...

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

class StickerMessage(_message.Message):
    __slots__ = ("sticker_id", "fast_preview", "image512", "image256", "sticker_collection_id", "sticker_collection_access_hash")
    STICKER_ID_FIELD_NUMBER: _ClassVar[int]
    FAST_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    IMAGE512_FIELD_NUMBER: _ClassVar[int]
    IMAGE256_FIELD_NUMBER: _ClassVar[int]
    STICKER_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    STICKER_COLLECTION_ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    sticker_id: _collections_pb2.Int32Value
    fast_preview: _collections_pb2.BytesValue
    image512: _files_pb2.ImageLocation
    image256: _files_pb2.ImageLocation
    sticker_collection_id: _collections_pb2.Int32Value
    sticker_collection_access_hash: _collections_pb2.Int64Value
    def __init__(self, sticker_id: _Optional[_Union[_collections_pb2.Int32Value, _Mapping]] = ..., fast_preview: _Optional[_Union[_collections_pb2.BytesValue, _Mapping]] = ..., image512: _Optional[_Union[_files_pb2.ImageLocation, _Mapping]] = ..., image256: _Optional[_Union[_files_pb2.ImageLocation, _Mapping]] = ..., sticker_collection_id: _Optional[_Union[_collections_pb2.Int32Value, _Mapping]] = ..., sticker_collection_access_hash: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ...) -> None: ...

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

class QuotedMessage(_message.Message):
    __slots__ = ("message_id", "sender_user_id", "message_date", "quoted_message_content", "quoted_peer")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_DATE_FIELD_NUMBER: _ClassVar[int]
    QUOTED_MESSAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    QUOTED_PEER_FIELD_NUMBER: _ClassVar[int]
    message_id: _collections_pb2.Int64Value
    sender_user_id: int
    message_date: int
    quoted_message_content: Message
    quoted_peer: _peers_pb2.OutPeer
    def __init__(self, message_id: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ..., sender_user_id: _Optional[int] = ..., message_date: _Optional[int] = ..., quoted_message_content: _Optional[_Union[Message, _Mapping]] = ..., quoted_peer: _Optional[_Union[_peers_pb2.OutPeer, _Mapping]] = ...) -> None: ...

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
    peer: _peers_pb2.Peer
    random_id: int
    date: _collections_pb2.Int64Value
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., random_id: _Optional[int] = ..., date: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class SingleMedia(_message.Message):
    __slots__ = ("random_id", "media")
    RANDOM_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    random_id: int
    media: DocumentMessage
    def __init__(self, random_id: _Optional[int] = ..., media: _Optional[_Union[DocumentMessage, _Mapping]] = ...) -> None: ...

class Dialog(_message.Message):
    __slots__ = ("peer", "unread_count", "sort_date", "sender_uid", "rid", "date", "message", "state", "first_unread_date", "ex_info", "is_message_forwarded", "marked_as_unread", "is_mute")
    PEER_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    SORT_DATE_FIELD_NUMBER: _ClassVar[int]
    SENDER_UID_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_UNREAD_DATE_FIELD_NUMBER: _ClassVar[int]
    EX_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_MESSAGE_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    MARKED_AS_UNREAD_FIELD_NUMBER: _ClassVar[int]
    IS_MUTE_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    unread_count: int
    sort_date: int
    sender_uid: int
    rid: int
    date: int
    message: Message
    state: int
    first_unread_date: _collections_pb2.Int64Value
    ex_info: _peers_pb2.ExInfo
    is_message_forwarded: bool
    marked_as_unread: bool
    is_mute: bool
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., unread_count: _Optional[int] = ..., sort_date: _Optional[int] = ..., sender_uid: _Optional[int] = ..., rid: _Optional[int] = ..., date: _Optional[int] = ..., message: _Optional[_Union[Message, _Mapping]] = ..., state: _Optional[int] = ..., first_unread_date: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ..., ex_info: _Optional[_Union[_peers_pb2.ExInfo, _Mapping]] = ..., is_message_forwarded: bool = ..., marked_as_unread: bool = ..., is_mute: bool = ...) -> None: ...
