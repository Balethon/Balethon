from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

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

class Restriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTRICTION_PRIVATE: _ClassVar[Restriction]
    RESTRICTION_PUBLIC: _ClassVar[Restriction]

class GroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROUP_TYPE_GROUP: _ClassVar[GroupType]
    GROUP_TYPE_CHANNEL: _ClassVar[GroupType]
    GROUP_TYPE_SUPER_GROUP: _ClassVar[GroupType]

class ExPeerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EX_PEER_TYPE_UNKNOWN: _ClassVar[ExPeerType]
    EX_PEER_TYPE_PRIVATE: _ClassVar[ExPeerType]
    EX_PEER_TYPE_GROUP: _ClassVar[ExPeerType]
    EX_PEER_TYPE_CHANNEL: _ClassVar[ExPeerType]
    EX_PEER_TYPE_BOT: _ClassVar[ExPeerType]
    EX_PEER_TYPE_SUPERGROUP: _ClassVar[ExPeerType]
    EX_PEER_TYPE_THREAD: _ClassVar[ExPeerType]

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

class Sex(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEX_UNKNOWN: _ClassVar[Sex]
    SEX_MALE: _ClassVar[Sex]
    SEX_FEMALE: _ClassVar[Sex]

class PollType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POLL_TYPE_SINGLE_CHOICE: _ClassVar[PollType]
    POLL_TYPE_MULTIPLE_CHOICE: _ClassVar[PollType]

class UpdateOptimization(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_OPTIMIZATION_UNKNOWN: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_NONE: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_STRIP_ENTITIES: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_ENABLE_COMBINED: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_FASTER_MESSAGES: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_STRIP_COUNTERS: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_COMPACT_USERS: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_GROUPS_V2: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_STRIP_MESSAGES: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_STRIP_USER_UPDATES: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_STRIP_TOTAL_UPDATES: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_STRIP_UNREAD_COUNTS: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_WITH_DATE: _ClassVar[UpdateOptimization]
    UPDATE_OPTIMIZATION_STRIP_UNREAD_STATE: _ClassVar[UpdateOptimization]

class StoryContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORY_CONTENT_TYPE_PHOTO: _ClassVar[StoryContentType]
    STORY_CONTENT_TYPE_VIDEO: _ClassVar[StoryContentType]
    STORY_CONTENT_TYPE_TEXT: _ClassVar[StoryContentType]

class StoryReactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORY_REACTION_TYPE_UNKNOWN: _ClassVar[StoryReactionType]
    STORY_REACTION_TYPE_VIEW: _ClassVar[StoryReactionType]
    STORY_REACTION_TYPE_EMOJI: _ClassVar[StoryReactionType]
    STORY_REACTION_TYPE_REMOVE_EMOJI: _ClassVar[StoryReactionType]
    STORY_REACTION_TYPE_LINK: _ClassVar[StoryReactionType]

class WidgetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIDGET_TYPE_UNKNOWN: _ClassVar[WidgetType]
    WIDGET_TYPE_LINK: _ClassVar[WidgetType]
    WIDGET_TYPE_POLL: _ClassVar[WidgetType]
    WIDGET_TYPE_POST: _ClassVar[WidgetType]
    WIDGET_TYPE_RESTORY: _ClassVar[WidgetType]

class ExceptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXCEPTION_TYPE_UNKNOWN: _ClassVar[ExceptionType]
    EXCEPTION_TYPE_EXCLUDE: _ClassVar[ExceptionType]
    EXCEPTION_TYPE_INCLUDE: _ClassVar[ExceptionType]
    EXCEPTION_TYPE_CONTACT: _ClassVar[ExceptionType]
    EXCEPTION_TYPE_ALL: _ClassVar[ExceptionType]

class StoryOptimization(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORY_OPTIMIZATION_UNKNOWN: _ClassVar[StoryOptimization]
    STORY_OPTIMIZATION_SPECIAL_STORIES_LIST: _ClassVar[StoryOptimization]

class StoryExpirationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORY_EXPIRATION_TYPE_ONE_DAY: _ClassVar[StoryExpirationType]
    STORY_EXPIRATION_TYPE_TWO_DAYS: _ClassVar[StoryExpirationType]

class StoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORY_TYPE_USER: _ClassVar[StoryType]
    STORY_TYPE_CHANNEL: _ClassVar[StoryType]
    STORY_TYPE_BOT: _ClassVar[StoryType]

class InlineCallbackAnswerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PIN: _ClassVar[InlineCallbackAnswerType]
    ALERT: _ClassVar[InlineCallbackAnswerType]

class SearchContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_CONTENTTYPE_ANY: _ClassVar[SearchContentType]
    SEARCH_CONTENTTYPE_TEXT: _ClassVar[SearchContentType]
    SEARCH_CONTENTTYPE_LINKS: _ClassVar[SearchContentType]
    SEARCH_CONTENTTYPE_DOCUMENTS: _ClassVar[SearchContentType]
    SEARCH_CONTENTTYPE_PHOTOS: _ClassVar[SearchContentType]
    SEARCH_CONTENTTYPE_VIDEOS: _ClassVar[SearchContentType]
    SEARCH_CONTENTTYPE_AUDIOS: _ClassVar[SearchContentType]
    SEARCH_CONTENTTYPE_VOICES: _ClassVar[SearchContentType]
    SEARCH_CONTENTTYPE_MEDIA: _ClassVar[SearchContentType]

class SearchPeerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_PEER_TYPE_GROUPS: _ClassVar[SearchPeerType]
    SEARCH_PEER_TYPE_CONTACTS: _ClassVar[SearchPeerType]
    SEARCH_PEER_TYPE_PUBLIC: _ClassVar[SearchPeerType]

class SearchMessageScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_MESSAGE_SCOPE_SCOPE_ALL: _ClassVar[SearchMessageScope]
    SEARCH_MESSAGE_SCOPE_SCOPE_PRIVATE: _ClassVar[SearchMessageScope]
    SEARCH_MESSAGE_SCOPE_SCOPE_GROUP: _ClassVar[SearchMessageScope]
    SEARCH_MESSAGE_SCOPE_SCOPE_CHANNEL: _ClassVar[SearchMessageScope]
    SEARCH_MESSAGE_SCOPE_SCOPE_BOT: _ClassVar[SearchMessageScope]
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
RESTRICTION_PRIVATE: Restriction
RESTRICTION_PUBLIC: Restriction
GROUP_TYPE_GROUP: GroupType
GROUP_TYPE_CHANNEL: GroupType
GROUP_TYPE_SUPER_GROUP: GroupType
EX_PEER_TYPE_UNKNOWN: ExPeerType
EX_PEER_TYPE_PRIVATE: ExPeerType
EX_PEER_TYPE_GROUP: ExPeerType
EX_PEER_TYPE_CHANNEL: ExPeerType
EX_PEER_TYPE_BOT: ExPeerType
EX_PEER_TYPE_SUPERGROUP: ExPeerType
EX_PEER_TYPE_THREAD: ExPeerType
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
SEX_UNKNOWN: Sex
SEX_MALE: Sex
SEX_FEMALE: Sex
POLL_TYPE_SINGLE_CHOICE: PollType
POLL_TYPE_MULTIPLE_CHOICE: PollType
UPDATE_OPTIMIZATION_UNKNOWN: UpdateOptimization
UPDATE_OPTIMIZATION_NONE: UpdateOptimization
UPDATE_OPTIMIZATION_STRIP_ENTITIES: UpdateOptimization
UPDATE_OPTIMIZATION_ENABLE_COMBINED: UpdateOptimization
UPDATE_OPTIMIZATION_FASTER_MESSAGES: UpdateOptimization
UPDATE_OPTIMIZATION_STRIP_COUNTERS: UpdateOptimization
UPDATE_OPTIMIZATION_COMPACT_USERS: UpdateOptimization
UPDATE_OPTIMIZATION_GROUPS_V2: UpdateOptimization
UPDATE_OPTIMIZATION_STRIP_MESSAGES: UpdateOptimization
UPDATE_OPTIMIZATION_STRIP_USER_UPDATES: UpdateOptimization
UPDATE_OPTIMIZATION_STRIP_TOTAL_UPDATES: UpdateOptimization
UPDATE_OPTIMIZATION_STRIP_UNREAD_COUNTS: UpdateOptimization
UPDATE_OPTIMIZATION_WITH_DATE: UpdateOptimization
UPDATE_OPTIMIZATION_STRIP_UNREAD_STATE: UpdateOptimization
STORY_CONTENT_TYPE_PHOTO: StoryContentType
STORY_CONTENT_TYPE_VIDEO: StoryContentType
STORY_CONTENT_TYPE_TEXT: StoryContentType
STORY_REACTION_TYPE_UNKNOWN: StoryReactionType
STORY_REACTION_TYPE_VIEW: StoryReactionType
STORY_REACTION_TYPE_EMOJI: StoryReactionType
STORY_REACTION_TYPE_REMOVE_EMOJI: StoryReactionType
STORY_REACTION_TYPE_LINK: StoryReactionType
WIDGET_TYPE_UNKNOWN: WidgetType
WIDGET_TYPE_LINK: WidgetType
WIDGET_TYPE_POLL: WidgetType
WIDGET_TYPE_POST: WidgetType
WIDGET_TYPE_RESTORY: WidgetType
EXCEPTION_TYPE_UNKNOWN: ExceptionType
EXCEPTION_TYPE_EXCLUDE: ExceptionType
EXCEPTION_TYPE_INCLUDE: ExceptionType
EXCEPTION_TYPE_CONTACT: ExceptionType
EXCEPTION_TYPE_ALL: ExceptionType
STORY_OPTIMIZATION_UNKNOWN: StoryOptimization
STORY_OPTIMIZATION_SPECIAL_STORIES_LIST: StoryOptimization
STORY_EXPIRATION_TYPE_ONE_DAY: StoryExpirationType
STORY_EXPIRATION_TYPE_TWO_DAYS: StoryExpirationType
STORY_TYPE_USER: StoryType
STORY_TYPE_CHANNEL: StoryType
STORY_TYPE_BOT: StoryType
PIN: InlineCallbackAnswerType
ALERT: InlineCallbackAnswerType
SEARCH_CONTENTTYPE_ANY: SearchContentType
SEARCH_CONTENTTYPE_TEXT: SearchContentType
SEARCH_CONTENTTYPE_LINKS: SearchContentType
SEARCH_CONTENTTYPE_DOCUMENTS: SearchContentType
SEARCH_CONTENTTYPE_PHOTOS: SearchContentType
SEARCH_CONTENTTYPE_VIDEOS: SearchContentType
SEARCH_CONTENTTYPE_AUDIOS: SearchContentType
SEARCH_CONTENTTYPE_VOICES: SearchContentType
SEARCH_CONTENTTYPE_MEDIA: SearchContentType
SEARCH_PEER_TYPE_GROUPS: SearchPeerType
SEARCH_PEER_TYPE_CONTACTS: SearchPeerType
SEARCH_PEER_TYPE_PUBLIC: SearchPeerType
SEARCH_MESSAGE_SCOPE_SCOPE_ALL: SearchMessageScope
SEARCH_MESSAGE_SCOPE_SCOPE_PRIVATE: SearchMessageScope
SEARCH_MESSAGE_SCOPE_SCOPE_GROUP: SearchMessageScope
SEARCH_MESSAGE_SCOPE_SCOPE_CHANNEL: SearchMessageScope
SEARCH_MESSAGE_SCOPE_SCOPE_BOT: SearchMessageScope
