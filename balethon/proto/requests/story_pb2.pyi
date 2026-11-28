from .. import enums_pb2 as _enums_pb2
from ..structs import peers_pb2 as _peers_pb2
from ..structs import story_pb2 as _story_pb2
from ..structs import collections_pb2 as _collections_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllStories(_message.Message):
    __slots__ = ("optimization",)
    OPTIMIZATION_FIELD_NUMBER: _ClassVar[int]
    optimization: _enums_pb2.StoryOptimization
    def __init__(self, optimization: _Optional[_Union[_enums_pb2.StoryOptimization, str]] = ...) -> None: ...

class GetStoryById(_message.Message):
    __slots__ = ("story_id",)
    STORY_ID_FIELD_NUMBER: _ClassVar[int]
    story_id: str
    def __init__(self, story_id: _Optional[str] = ...) -> None: ...

class GetStoriesByList(_message.Message):
    __slots__ = ("ex_peers",)
    EX_PEERS_FIELD_NUMBER: _ClassVar[int]
    ex_peers: _containers.RepeatedCompositeFieldContainer[_peers_pb2.ExPeer]
    def __init__(self, ex_peers: _Optional[_Iterable[_Union[_peers_pb2.ExPeer, _Mapping]]] = ...) -> None: ...

class GetStories(_message.Message):
    __slots__ = ("get_unmutual",)
    GET_UNMUTUAL_FIELD_NUMBER: _ClassVar[int]
    get_unmutual: _collections_pb2.BoolValue
    def __init__(self, get_unmutual: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class GetChannelStories(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStoryReactionEmojis(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDefaultStoryBackgrounds(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStoryTags(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMostPopularStories(_message.Message):
    __slots__ = ("get_special_stories", "optimization")
    GET_SPECIAL_STORIES_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_FIELD_NUMBER: _ClassVar[int]
    get_special_stories: _collections_pb2.BoolValue
    optimization: _enums_pb2.StoryOptimization
    def __init__(self, get_special_stories: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ..., optimization: _Optional[_Union[_enums_pb2.StoryOptimization, str]] = ...) -> None: ...

class GetViewers(_message.Message):
    __slots__ = ("story_id", "pagination")
    STORY_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    story_id: str
    pagination: _story_pb2.ViewersPagination
    def __init__(self, story_id: _Optional[str] = ..., pagination: _Optional[_Union[_story_pb2.ViewersPagination, _Mapping]] = ...) -> None: ...

class GetViewersCount(_message.Message):
    __slots__ = ("story_id",)
    STORY_ID_FIELD_NUMBER: _ClassVar[int]
    story_id: str
    def __init__(self, story_id: _Optional[str] = ...) -> None: ...

class GetStoryWidgets(_message.Message):
    __slots__ = ("story_id",)
    STORY_ID_FIELD_NUMBER: _ClassVar[int]
    story_id: str
    def __init__(self, story_id: _Optional[str] = ...) -> None: ...

class AddStory(_message.Message):
    __slots__ = ("media_story", "text_story", "tag_ids", "expiration_type")
    MEDIA_STORY_FIELD_NUMBER: _ClassVar[int]
    TEXT_STORY_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    media_story: _story_pb2.MediaStory
    text_story: _story_pb2.TextStory
    tag_ids: _containers.RepeatedScalarFieldContainer[int]
    expiration_type: _enums_pb2.StoryExpirationType
    def __init__(self, media_story: _Optional[_Union[_story_pb2.MediaStory, _Mapping]] = ..., text_story: _Optional[_Union[_story_pb2.TextStory, _Mapping]] = ..., tag_ids: _Optional[_Iterable[int]] = ..., expiration_type: _Optional[_Union[_enums_pb2.StoryExpirationType, str]] = ...) -> None: ...

class AddBotStory(_message.Message):
    __slots__ = ("ex_peer", "media_story", "text_story", "tag_ids", "expiration_type")
    EX_PEER_FIELD_NUMBER: _ClassVar[int]
    MEDIA_STORY_FIELD_NUMBER: _ClassVar[int]
    TEXT_STORY_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ex_peer: _peers_pb2.ExPeer
    media_story: _story_pb2.MediaStory
    text_story: _story_pb2.TextStory
    tag_ids: _containers.RepeatedScalarFieldContainer[int]
    expiration_type: _enums_pb2.StoryExpirationType
    def __init__(self, ex_peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ..., media_story: _Optional[_Union[_story_pb2.MediaStory, _Mapping]] = ..., text_story: _Optional[_Union[_story_pb2.TextStory, _Mapping]] = ..., tag_ids: _Optional[_Iterable[int]] = ..., expiration_type: _Optional[_Union[_enums_pb2.StoryExpirationType, str]] = ...) -> None: ...

class AddChannelStory(_message.Message):
    __slots__ = ("ex_peer", "has_reply", "tag_ids", "expiration_type", "media_story", "text_story")
    EX_PEER_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLY_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_STORY_FIELD_NUMBER: _ClassVar[int]
    TEXT_STORY_FIELD_NUMBER: _ClassVar[int]
    ex_peer: _peers_pb2.ExPeer
    has_reply: bool
    tag_ids: _containers.RepeatedScalarFieldContainer[int]
    expiration_type: _enums_pb2.StoryExpirationType
    media_story: _story_pb2.MediaStory
    text_story: _story_pb2.TextStory
    def __init__(self, ex_peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ..., has_reply: bool = ..., tag_ids: _Optional[_Iterable[int]] = ..., expiration_type: _Optional[_Union[_enums_pb2.StoryExpirationType, str]] = ..., media_story: _Optional[_Union[_story_pb2.MediaStory, _Mapping]] = ..., text_story: _Optional[_Union[_story_pb2.TextStory, _Mapping]] = ...) -> None: ...

class ReactToStory(_message.Message):
    __slots__ = ("story_id", "reaction", "type", "reaction_type", "reaction_text")
    STORY_ID_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    story_id: str
    reaction: str
    type: _enums_pb2.StoryType
    reaction_type: _enums_pb2.StoryReactionType
    reaction_text: _collections_pb2.StringValue
    def __init__(self, story_id: _Optional[str] = ..., reaction: _Optional[str] = ..., type: _Optional[_Union[_enums_pb2.StoryType, str]] = ..., reaction_type: _Optional[_Union[_enums_pb2.StoryReactionType, str]] = ..., reaction_text: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ...) -> None: ...

class CheckLinkValidity(_message.Message):
    __slots__ = ("ex_peer", "link")
    EX_PEER_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    ex_peer: _peers_pb2.ExPeer
    link: str
    def __init__(self, ex_peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ..., link: _Optional[str] = ...) -> None: ...

class RemoveStory(_message.Message):
    __slots__ = ("story_id",)
    STORY_ID_FIELD_NUMBER: _ClassVar[int]
    story_id: str
    def __init__(self, story_id: _Optional[str] = ...) -> None: ...
