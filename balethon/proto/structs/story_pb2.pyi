from ..structs import collections_pb2 as _collections_pb2
from ..structs import files_pb2 as _files_pb2
from ..structs import peers_pb2 as _peers_pb2
from .. import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Coordinate(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class LinkWidget(_message.Message):
    __slots__ = ("link", "title")
    LINK_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    link: str
    title: str
    def __init__(self, link: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class PostWidget(_message.Message):
    __slots__ = ("link",)
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    def __init__(self, link: _Optional[str] = ...) -> None: ...

class ReStoryWidget(_message.Message):
    __slots__ = ("story_id", "ex_peer")
    STORY_ID_FIELD_NUMBER: _ClassVar[int]
    EX_PEER_FIELD_NUMBER: _ClassVar[int]
    story_id: str
    ex_peer: _peers_pb2.ExPeer
    def __init__(self, story_id: _Optional[str] = ..., ex_peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ...) -> None: ...

class PollWidget(_message.Message):
    __slots__ = ("question",)
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: str
    def __init__(self, question: _Optional[str] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("coordinates",)
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    coordinates: _containers.RepeatedCompositeFieldContainer[Coordinate]
    def __init__(self, coordinates: _Optional[_Iterable[_Union[Coordinate, _Mapping]]] = ...) -> None: ...

class VideoStory(_message.Message):
    __slots__ = ("file_location", "fast_thumb", "file_size", "duration", "format")
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    FAST_THUMB_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    file_location: _files_pb2.FileLocation
    fast_thumb: _files_pb2.FastThumb
    file_size: int
    duration: float
    format: str
    def __init__(self, file_location: _Optional[_Union[_files_pb2.FileLocation, _Mapping]] = ..., fast_thumb: _Optional[_Union[_files_pb2.FastThumb, _Mapping]] = ..., file_size: _Optional[int] = ..., duration: _Optional[float] = ..., format: _Optional[str] = ...) -> None: ...

class Widget(_message.Message):
    __slots__ = ("id", "type", "position", "link_widget", "poll_widget", "post_widget", "restory_widget")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    LINK_WIDGET_FIELD_NUMBER: _ClassVar[int]
    POLL_WIDGET_FIELD_NUMBER: _ClassVar[int]
    POST_WIDGET_FIELD_NUMBER: _ClassVar[int]
    RESTORY_WIDGET_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: _enums_pb2.WidgetType
    position: Position
    link_widget: LinkWidget
    poll_widget: PollWidget
    post_widget: PostWidget
    restory_widget: ReStoryWidget
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[_enums_pb2.WidgetType, str]] = ..., position: _Optional[_Union[Position, _Mapping]] = ..., link_widget: _Optional[_Union[LinkWidget, _Mapping]] = ..., poll_widget: _Optional[_Union[PollWidget, _Mapping]] = ..., post_widget: _Optional[_Union[PostWidget, _Mapping]] = ..., restory_widget: _Optional[_Union[ReStoryWidget, _Mapping]] = ...) -> None: ...

class StoryReaction(_message.Message):
    __slots__ = ("reaction_type", "reaction_text")
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    reaction_type: _enums_pb2.StoryReactionType
    reaction_text: _collections_pb2.StringValue
    def __init__(self, reaction_type: _Optional[_Union[_enums_pb2.StoryReactionType, str]] = ..., reaction_text: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ...) -> None: ...

class TextConfig(_message.Message):
    __slots__ = ("text_font", "background_color", "text_color")
    TEXT_FONT_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    text_font: str
    background_color: str
    text_color: str
    def __init__(self, text_font: _Optional[str] = ..., background_color: _Optional[str] = ..., text_color: _Optional[str] = ...) -> None: ...

class MediaStory(_message.Message):
    __slots__ = ("file_location", "fast_thumb", "file_size", "video", "widget")
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    FAST_THUMB_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    WIDGET_FIELD_NUMBER: _ClassVar[int]
    file_location: _files_pb2.FileLocation
    fast_thumb: _files_pb2.FastThumb
    file_size: int
    video: VideoStory
    widget: _containers.RepeatedCompositeFieldContainer[Widget]
    def __init__(self, file_location: _Optional[_Union[_files_pb2.FileLocation, _Mapping]] = ..., fast_thumb: _Optional[_Union[_files_pb2.FastThumb, _Mapping]] = ..., file_size: _Optional[int] = ..., video: _Optional[_Union[VideoStory, _Mapping]] = ..., widget: _Optional[_Iterable[_Union[Widget, _Mapping]]] = ...) -> None: ...

class TextStory(_message.Message):
    __slots__ = ("text", "config")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    text: str
    config: TextConfig
    def __init__(self, text: _Optional[str] = ..., config: _Optional[_Union[TextConfig, _Mapping]] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("id", "title", "color")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    color: str
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class StoryContent(_message.Message):
    __slots__ = ("media", "text")
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    media: MediaStory
    text: TextStory
    def __init__(self, media: _Optional[_Union[MediaStory, _Mapping]] = ..., text: _Optional[_Union[TextStory, _Mapping]] = ...) -> None: ...

class ChannelStory(_message.Message):
    __slots__ = ("id", "owner_user_id", "reaction", "created_at", "story_content", "has_reply", "ex_peer", "has_widget", "tag_ids", "story_content_type", "reactions", "is_hidden", "story_tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STORY_CONTENT_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLY_FIELD_NUMBER: _ClassVar[int]
    EX_PEER_FIELD_NUMBER: _ClassVar[int]
    HAS_WIDGET_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    STORY_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    STORY_TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner_user_id: int
    reaction: _collections_pb2.StringValue
    created_at: int
    story_content: MediaStory
    has_reply: bool
    ex_peer: _peers_pb2.ExPeer
    has_widget: bool
    tag_ids: _containers.RepeatedScalarFieldContainer[int]
    story_content_type: _enums_pb2.StoryContentType
    reactions: _containers.RepeatedCompositeFieldContainer[StoryReaction]
    is_hidden: bool
    story_tags: Tag
    def __init__(self, id: _Optional[str] = ..., owner_user_id: _Optional[int] = ..., reaction: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., created_at: _Optional[int] = ..., story_content: _Optional[_Union[MediaStory, _Mapping]] = ..., has_reply: bool = ..., ex_peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ..., has_widget: bool = ..., tag_ids: _Optional[_Iterable[int]] = ..., story_content_type: _Optional[_Union[_enums_pb2.StoryContentType, str]] = ..., reactions: _Optional[_Iterable[_Union[StoryReaction, _Mapping]]] = ..., is_hidden: bool = ..., story_tags: _Optional[_Union[Tag, _Mapping]] = ...) -> None: ...

class Story(_message.Message):
    __slots__ = ("id", "owner_user_id", "reaction", "created_at", "story_content", "has_widget", "has_reply", "is_hidden", "is_mutual", "tag_ids", "story_content_type", "reactions", "exception_type", "story_tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STORY_CONTENT_FIELD_NUMBER: _ClassVar[int]
    HAS_WIDGET_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLY_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    IS_MUTUAL_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    STORY_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORY_TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner_user_id: int
    reaction: _collections_pb2.StringValue
    created_at: int
    story_content: StoryContent
    has_widget: bool
    has_reply: bool
    is_hidden: bool
    is_mutual: bool
    tag_ids: _containers.RepeatedScalarFieldContainer[int]
    story_content_type: _enums_pb2.StoryContentType
    reactions: _containers.RepeatedCompositeFieldContainer[StoryReaction]
    exception_type: _enums_pb2.ExceptionType
    story_tags: Tag
    def __init__(self, id: _Optional[str] = ..., owner_user_id: _Optional[int] = ..., reaction: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., created_at: _Optional[int] = ..., story_content: _Optional[_Union[StoryContent, _Mapping]] = ..., has_widget: bool = ..., has_reply: bool = ..., is_hidden: bool = ..., is_mutual: bool = ..., tag_ids: _Optional[_Iterable[int]] = ..., story_content_type: _Optional[_Union[_enums_pb2.StoryContentType, str]] = ..., reactions: _Optional[_Iterable[_Union[StoryReaction, _Mapping]]] = ..., exception_type: _Optional[_Union[_enums_pb2.ExceptionType, str]] = ..., story_tags: _Optional[_Union[Tag, _Mapping]] = ...) -> None: ...

class BotStory(_message.Message):
    __slots__ = ("id", "owner_user_id", "reaction", "created_at", "story_content", "has_reply", "ex_peer", "has_widget", "tag_ids", "story_content_type", "reactions", "is_hidden", "story_tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STORY_CONTENT_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLY_FIELD_NUMBER: _ClassVar[int]
    EX_PEER_FIELD_NUMBER: _ClassVar[int]
    HAS_WIDGET_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    STORY_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    STORY_TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner_user_id: int
    reaction: _collections_pb2.StringValue
    created_at: int
    story_content: MediaStory
    has_reply: bool
    ex_peer: _peers_pb2.ExPeer
    has_widget: bool
    tag_ids: _containers.RepeatedScalarFieldContainer[int]
    story_content_type: _enums_pb2.StoryContentType
    reactions: _containers.RepeatedCompositeFieldContainer[StoryReaction]
    is_hidden: bool
    story_tags: Tag
    def __init__(self, id: _Optional[str] = ..., owner_user_id: _Optional[int] = ..., reaction: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., created_at: _Optional[int] = ..., story_content: _Optional[_Union[MediaStory, _Mapping]] = ..., has_reply: bool = ..., ex_peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ..., has_widget: bool = ..., tag_ids: _Optional[_Iterable[int]] = ..., story_content_type: _Optional[_Union[_enums_pb2.StoryContentType, str]] = ..., reactions: _Optional[_Iterable[_Union[StoryReaction, _Mapping]]] = ..., is_hidden: bool = ..., story_tags: _Optional[_Union[Tag, _Mapping]] = ...) -> None: ...

class ExPeerPopularity(_message.Message):
    __slots__ = ("ex_peer", "popularity")
    EX_PEER_FIELD_NUMBER: _ClassVar[int]
    POPULARITY_FIELD_NUMBER: _ClassVar[int]
    ex_peer: _peers_pb2.ExPeer
    popularity: float
    def __init__(self, ex_peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ..., popularity: _Optional[float] = ...) -> None: ...

class ViewersPagination(_message.Message):
    __slots__ = ("page", "limit")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    page: int
    limit: int
    def __init__(self, page: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class Emoji(_message.Message):
    __slots__ = ("emoji",)
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    emoji: str
    def __init__(self, emoji: _Optional[str] = ...) -> None: ...

class Viewer(_message.Message):
    __slots__ = ("reaction", "user_id", "reacted_at", "reaction_data")
    REACTION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    REACTED_AT_FIELD_NUMBER: _ClassVar[int]
    REACTION_DATA_FIELD_NUMBER: _ClassVar[int]
    reaction: str
    user_id: int
    reacted_at: int
    reaction_data: _containers.RepeatedCompositeFieldContainer[StoryReaction]
    def __init__(self, reaction: _Optional[str] = ..., user_id: _Optional[int] = ..., reacted_at: _Optional[int] = ..., reaction_data: _Optional[_Iterable[_Union[StoryReaction, _Mapping]]] = ...) -> None: ...
