from ..structs import collections_pb2 as _collections_pb2
from ..structs import files_pb2 as _files_pb2
from ..structs import peers_pb2 as _peers_pb2
from ..enums import users_pb2 as _users_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IntroPhoto(_message.Message):
    __slots__ = ("thumb", "width", "height")
    THUMB_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    thumb: _files_pb2.FastThumb
    width: int
    height: int
    def __init__(self, thumb: _Optional[_Union[_files_pb2.FastThumb, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class IntroGif(_message.Message):
    __slots__ = ("thumb", "width", "height")
    THUMB_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    thumb: _files_pb2.FastThumb
    width: int
    height: int
    def __init__(self, thumb: _Optional[_Union[_files_pb2.FastThumb, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

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
    file_location: _files_pb2.FileLocation
    file_size: int
    mime_type: str
    file_name: str
    media_extra: MediaExt
    def __init__(self, file_location: _Optional[_Union[_files_pb2.FileLocation, _Mapping]] = ..., file_size: _Optional[int] = ..., mime_type: _Optional[str] = ..., file_name: _Optional[str] = ..., media_extra: _Optional[_Union[MediaExt, _Mapping]] = ...) -> None: ...

class IntroMessage(_message.Message):
    __slots__ = ("text", "media")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    text: _collections_pb2.StringValue
    media: IntroMedia
    def __init__(self, text: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., media: _Optional[_Union[IntroMedia, _Mapping]] = ...) -> None: ...

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
    text: _collections_pb2.StringValue
    file_location: _files_pb2.FileLocation
    width: int
    height: int
    file_size: int
    mime_type: str
    file_name: str
    thumb: _files_pb2.FastThumb
    def __init__(self, text: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., file_location: _Optional[_Union[_files_pb2.FileLocation, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., file_size: _Optional[int] = ..., mime_type: _Optional[str] = ..., file_name: _Optional[str] = ..., thumb: _Optional[_Union[_files_pb2.FastThumb, _Mapping]] = ...) -> None: ...

class BotExInfo(_message.Message):
    __slots__ = ("bot_active_users", "has_main_mini_app", "intro", "intro_message", "has_timche_profile")
    BOT_ACTIVE_USERS_FIELD_NUMBER: _ClassVar[int]
    HAS_MAIN_MINI_APP_FIELD_NUMBER: _ClassVar[int]
    INTRO_FIELD_NUMBER: _ClassVar[int]
    INTRO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HAS_TIMCHE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    bot_active_users: _collections_pb2.StringValue
    has_main_mini_app: _collections_pb2.BoolValue
    intro: Intro
    intro_message: IntroMessage
    has_timche_profile: _collections_pb2.BoolValue
    def __init__(self, bot_active_users: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., has_main_mini_app: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ..., intro: _Optional[_Union[Intro, _Mapping]] = ..., intro_message: _Optional[_Union[IntroMessage, _Mapping]] = ..., has_timche_profile: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ...) -> None: ...

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
    local_name: _collections_pb2.StringValue
    sex: _users_pb2.Sex
    avatar: _files_pb2.Avatar
    is_bot: _collections_pb2.BoolValue
    nick: _collections_pb2.StringValue
    is_deleted: _collections_pb2.BoolValue
    created_at: _collections_pb2.Int64Value
    ex_info: _peers_pb2.ExInfo
    bot_ex_info: BotExInfo
    def __init__(self, id: _Optional[int] = ..., access_hash: _Optional[int] = ..., name: _Optional[str] = ..., local_name: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., sex: _Optional[_Union[_users_pb2.Sex, str]] = ..., avatar: _Optional[_Union[_files_pb2.Avatar, _Mapping]] = ..., is_bot: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ..., nick: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., is_deleted: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ..., created_at: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ..., ex_info: _Optional[_Union[_peers_pb2.ExInfo, _Mapping]] = ..., bot_ex_info: _Optional[_Union[BotExInfo, _Mapping]] = ...) -> None: ...
