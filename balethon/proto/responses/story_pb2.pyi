from ..structs import story_pb2 as _story_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllStories(_message.Message):
    __slots__ = ("user_stories", "channel_stories", "bot_stories", "popularity_list", "most_popular_stories")
    USER_STORIES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_STORIES_FIELD_NUMBER: _ClassVar[int]
    BOT_STORIES_FIELD_NUMBER: _ClassVar[int]
    POPULARITY_LIST_FIELD_NUMBER: _ClassVar[int]
    MOST_POPULAR_STORIES_FIELD_NUMBER: _ClassVar[int]
    user_stories: _containers.RepeatedCompositeFieldContainer[_story_pb2.Story]
    channel_stories: _containers.RepeatedCompositeFieldContainer[_story_pb2.ChannelStory]
    bot_stories: _containers.RepeatedCompositeFieldContainer[_story_pb2.BotStory]
    popularity_list: _containers.RepeatedCompositeFieldContainer[_story_pb2.ExPeerPopularity]
    most_popular_stories: _containers.RepeatedCompositeFieldContainer[_story_pb2.ChannelStory]
    def __init__(self, user_stories: _Optional[_Iterable[_Union[_story_pb2.Story, _Mapping]]] = ..., channel_stories: _Optional[_Iterable[_Union[_story_pb2.ChannelStory, _Mapping]]] = ..., bot_stories: _Optional[_Iterable[_Union[_story_pb2.BotStory, _Mapping]]] = ..., popularity_list: _Optional[_Iterable[_Union[_story_pb2.ExPeerPopularity, _Mapping]]] = ..., most_popular_stories: _Optional[_Iterable[_Union[_story_pb2.ChannelStory, _Mapping]]] = ...) -> None: ...

class GetStoryById(_message.Message):
    __slots__ = ("result", "channel_story_result", "bot_story_result")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_STORY_RESULT_FIELD_NUMBER: _ClassVar[int]
    BOT_STORY_RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _story_pb2.Story
    channel_story_result: _story_pb2.ChannelStory
    bot_story_result: _story_pb2.BotStory
    def __init__(self, result: _Optional[_Union[_story_pb2.Story, _Mapping]] = ..., channel_story_result: _Optional[_Union[_story_pb2.ChannelStory, _Mapping]] = ..., bot_story_result: _Optional[_Union[_story_pb2.BotStory, _Mapping]] = ...) -> None: ...

class GetStoriesByList(_message.Message):
    __slots__ = ("user_stories", "channel_stories", "bot_stories")
    USER_STORIES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_STORIES_FIELD_NUMBER: _ClassVar[int]
    BOT_STORIES_FIELD_NUMBER: _ClassVar[int]
    user_stories: _containers.RepeatedCompositeFieldContainer[_story_pb2.Story]
    channel_stories: _containers.RepeatedCompositeFieldContainer[_story_pb2.ChannelStory]
    bot_stories: _containers.RepeatedCompositeFieldContainer[_story_pb2.BotStory]
    def __init__(self, user_stories: _Optional[_Iterable[_Union[_story_pb2.Story, _Mapping]]] = ..., channel_stories: _Optional[_Iterable[_Union[_story_pb2.ChannelStory, _Mapping]]] = ..., bot_stories: _Optional[_Iterable[_Union[_story_pb2.BotStory, _Mapping]]] = ...) -> None: ...

class GetStories(_message.Message):
    __slots__ = ("result", "popularity_list")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    POPULARITY_LIST_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[_story_pb2.Story]
    popularity_list: _containers.RepeatedCompositeFieldContainer[_story_pb2.ExPeerPopularity]
    def __init__(self, result: _Optional[_Iterable[_Union[_story_pb2.Story, _Mapping]]] = ..., popularity_list: _Optional[_Iterable[_Union[_story_pb2.ExPeerPopularity, _Mapping]]] = ...) -> None: ...

class GetChannelStories(_message.Message):
    __slots__ = ("result", "popularity_list")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    POPULARITY_LIST_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[_story_pb2.ChannelStory]
    popularity_list: _containers.RepeatedCompositeFieldContainer[_story_pb2.ExPeerPopularity]
    def __init__(self, result: _Optional[_Iterable[_Union[_story_pb2.ChannelStory, _Mapping]]] = ..., popularity_list: _Optional[_Iterable[_Union[_story_pb2.ExPeerPopularity, _Mapping]]] = ...) -> None: ...

class GetStoryReactionEmojis(_message.Message):
    __slots__ = ("emojis",)
    EMOJIS_FIELD_NUMBER: _ClassVar[int]
    emojis: _containers.RepeatedCompositeFieldContainer[_story_pb2.Emoji]
    def __init__(self, emojis: _Optional[_Iterable[_Union[_story_pb2.Emoji, _Mapping]]] = ...) -> None: ...

class GetDefaultStoryBackgrounds(_message.Message):
    __slots__ = ("default_story_backgrounds",)
    DEFAULT_STORY_BACKGROUNDS_FIELD_NUMBER: _ClassVar[int]
    default_story_backgrounds: _containers.RepeatedCompositeFieldContainer[_story_pb2.MediaStory]
    def __init__(self, default_story_backgrounds: _Optional[_Iterable[_Union[_story_pb2.MediaStory, _Mapping]]] = ...) -> None: ...

class GetStoryTags(_message.Message):
    __slots__ = ("tags",)
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[_story_pb2.Tag]
    def __init__(self, tags: _Optional[_Iterable[_Union[_story_pb2.Tag, _Mapping]]] = ...) -> None: ...

class GetMostPopularStories(_message.Message):
    __slots__ = ("result", "popularity_list")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    POPULARITY_LIST_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[_story_pb2.ChannelStory]
    popularity_list: _containers.RepeatedCompositeFieldContainer[_story_pb2.ExPeerPopularity]
    def __init__(self, result: _Optional[_Iterable[_Union[_story_pb2.ChannelStory, _Mapping]]] = ..., popularity_list: _Optional[_Iterable[_Union[_story_pb2.ExPeerPopularity, _Mapping]]] = ...) -> None: ...

class GetViewers(_message.Message):
    __slots__ = ("viewers", "view_count", "like_count", "link_click_count", "emoji_count", "restory_count")
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIKE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LINK_CLICK_COUNT_FIELD_NUMBER: _ClassVar[int]
    EMOJI_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESTORY_COUNT_FIELD_NUMBER: _ClassVar[int]
    viewers: _containers.RepeatedCompositeFieldContainer[_story_pb2.Viewer]
    view_count: int
    like_count: int
    link_click_count: int
    emoji_count: int
    restory_count: int
    def __init__(self, viewers: _Optional[_Iterable[_Union[_story_pb2.Viewer, _Mapping]]] = ..., view_count: _Optional[int] = ..., like_count: _Optional[int] = ..., link_click_count: _Optional[int] = ..., emoji_count: _Optional[int] = ..., restory_count: _Optional[int] = ...) -> None: ...

class GetViewersCount(_message.Message):
    __slots__ = ("view_count", "like_count", "link_click_count", "emoji_count", "restory_count")
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIKE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LINK_CLICK_COUNT_FIELD_NUMBER: _ClassVar[int]
    EMOJI_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESTORY_COUNT_FIELD_NUMBER: _ClassVar[int]
    view_count: int
    like_count: int
    link_click_count: int
    emoji_count: int
    restory_count: int
    def __init__(self, view_count: _Optional[int] = ..., like_count: _Optional[int] = ..., link_click_count: _Optional[int] = ..., emoji_count: _Optional[int] = ..., restory_count: _Optional[int] = ...) -> None: ...

class GetStoryWidgets(_message.Message):
    __slots__ = ("widgets",)
    WIDGETS_FIELD_NUMBER: _ClassVar[int]
    widgets: _containers.RepeatedCompositeFieldContainer[_story_pb2.Widget]
    def __init__(self, widgets: _Optional[_Iterable[_Union[_story_pb2.Widget, _Mapping]]] = ...) -> None: ...

class AddStory(_message.Message):
    __slots__ = ("story_id",)
    STORY_ID_FIELD_NUMBER: _ClassVar[int]
    story_id: str
    def __init__(self, story_id: _Optional[str] = ...) -> None: ...

class CanAddBotStory(_message.Message):
    __slots__ = ("can_add_bot_story",)
    CAN_ADD_BOT_STORY_FIELD_NUMBER: _ClassVar[int]
    can_add_bot_story: bool
    def __init__(self, can_add_bot_story: bool = ...) -> None: ...
