from ..structs import peers_pb2 as _peers_pb2
from .. import enums_pb2 as _enums_pb2
from ..structs import collections_pb2 as _collections_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchAndCondition(_message.Message):
    __slots__ = ("and_query",)
    AND_QUERY_FIELD_NUMBER: _ClassVar[int]
    and_query: _containers.RepeatedCompositeFieldContainer[SearchCondition]
    def __init__(self, and_query: _Optional[_Iterable[_Union[SearchCondition, _Mapping]]] = ...) -> None: ...

class SearchOrCondition(_message.Message):
    __slots__ = ("or_query",)
    OR_QUERY_FIELD_NUMBER: _ClassVar[int]
    or_query: _containers.RepeatedCompositeFieldContainer[SearchCondition]
    def __init__(self, or_query: _Optional[_Iterable[_Union[SearchCondition, _Mapping]]] = ...) -> None: ...

class SearchPeerCondition(_message.Message):
    __slots__ = ("peer",)
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.OutPeer
    def __init__(self, peer: _Optional[_Union[_peers_pb2.OutPeer, _Mapping]] = ...) -> None: ...

class SearchPeerContentType(_message.Message):
    __slots__ = ("content_type",)
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    content_type: _enums_pb2.SearchContentType
    def __init__(self, content_type: _Optional[_Union[_enums_pb2.SearchContentType, str]] = ...) -> None: ...

class SearchPeerTypeCondition(_message.Message):
    __slots__ = ("peer_type",)
    PEER_TYPE_FIELD_NUMBER: _ClassVar[int]
    peer_type: _enums_pb2.SearchPeerType
    def __init__(self, peer_type: _Optional[_Union[_enums_pb2.SearchPeerType, str]] = ...) -> None: ...

class SearchPieceText(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class SearchDateCondition(_message.Message):
    __slots__ = ("date",)
    DATE_FIELD_NUMBER: _ClassVar[int]
    date: int
    def __init__(self, date: _Optional[int] = ...) -> None: ...

class SearchSenderCondition(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class SearchHasLinkCondition(_message.Message):
    __slots__ = ("has_link",)
    HAS_LINK_FIELD_NUMBER: _ClassVar[int]
    has_link: bool
    def __init__(self, has_link: bool = ...) -> None: ...

class SearchDocumentName(_message.Message):
    __slots__ = ("document_name",)
    DOCUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    document_name: str
    def __init__(self, document_name: _Optional[str] = ...) -> None: ...

class SearchScopeCondition(_message.Message):
    __slots__ = ("scope",)
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    scope: _enums_pb2.SearchMessageScope
    def __init__(self, scope: _Optional[_Union[_enums_pb2.SearchMessageScope, str]] = ...) -> None: ...

class SearchCategoryCondition(_message.Message):
    __slots__ = ("category_search_params",)
    CATEGORY_SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    category_search_params: bytes
    def __init__(self, category_search_params: _Optional[bytes] = ...) -> None: ...

class SearchCondition(_message.Message):
    __slots__ = ("search_and_condition", "search_or_condition", "search_peer_condition", "search_peer_content_type", "search_peer_type_condition", "search_piece_text", "search_date", "search_sender", "search_has_link", "search_document_name", "search_scope_condition", "search_category_condition")
    SEARCH_AND_CONDITION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_OR_CONDITION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PEER_CONDITION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PEER_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PEER_TYPE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PIECE_TEXT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_DATE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SENDER_FIELD_NUMBER: _ClassVar[int]
    SEARCH_HAS_LINK_FIELD_NUMBER: _ClassVar[int]
    SEARCH_DOCUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SCOPE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CATEGORY_CONDITION_FIELD_NUMBER: _ClassVar[int]
    search_and_condition: SearchAndCondition
    search_or_condition: SearchOrCondition
    search_peer_condition: SearchPeerCondition
    search_peer_content_type: SearchPeerContentType
    search_peer_type_condition: SearchPeerTypeCondition
    search_piece_text: SearchPieceText
    search_date: SearchDateCondition
    search_sender: SearchSenderCondition
    search_has_link: SearchHasLinkCondition
    search_document_name: SearchDocumentName
    search_scope_condition: SearchScopeCondition
    search_category_condition: SearchCategoryCondition
    def __init__(self, search_and_condition: _Optional[_Union[SearchAndCondition, _Mapping]] = ..., search_or_condition: _Optional[_Union[SearchOrCondition, _Mapping]] = ..., search_peer_condition: _Optional[_Union[SearchPeerCondition, _Mapping]] = ..., search_peer_content_type: _Optional[_Union[SearchPeerContentType, _Mapping]] = ..., search_peer_type_condition: _Optional[_Union[SearchPeerTypeCondition, _Mapping]] = ..., search_piece_text: _Optional[_Union[SearchPieceText, _Mapping]] = ..., search_date: _Optional[_Union[SearchDateCondition, _Mapping]] = ..., search_sender: _Optional[_Union[SearchSenderCondition, _Mapping]] = ..., search_has_link: _Optional[_Union[SearchHasLinkCondition, _Mapping]] = ..., search_document_name: _Optional[_Union[SearchDocumentName, _Mapping]] = ..., search_scope_condition: _Optional[_Union[SearchScopeCondition, _Mapping]] = ..., search_category_condition: _Optional[_Union[SearchCategoryCondition, _Mapping]] = ...) -> None: ...

class PeerSearchResult(_message.Message):
    __slots__ = ("peer", "title", "description", "members_count", "date_created", "creator", "is_public", "is_joined")
    PEER_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    IS_JOINED_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    title: str
    description: _collections_pb2.StringValue
    members_count: _collections_pb2.Int32Value
    date_created: _collections_pb2.Int64Value
    creator: _collections_pb2.Int32Value
    is_public: _collections_pb2.BoolValue
    is_joined: _collections_pb2.BoolValue
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., title: _Optional[str] = ..., description: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., members_count: _Optional[_Union[_collections_pb2.Int32Value, _Mapping]] = ..., date_created: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ..., creator: _Optional[_Union[_collections_pb2.Int32Value, _Mapping]] = ..., is_public: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ..., is_joined: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ...) -> None: ...
