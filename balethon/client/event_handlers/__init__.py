from .add_event_handler import AddEventHandler
from .on_callback_query import OnCallbackQuery
from .on_command import OnCommand
from .on_connect import OnConnect
from .on_disconnect import OnDisconnect
from .on_edited_message import OnEditedMessage
from .on_error import OnError
from .on_event import OnEvent
from .on_message import OnMessage
from .on_pre_checkout_query import OnPreCheckoutQuery
from .on_shipping_query import OnShippingQuery
from .on_initialize import OnInitialize
from .on_shutdown import OnShutdown
from .on_update import OnUpdate
from .remove_event_handler import RemoveEventHandler


class EventHandlers(
    AddEventHandler,
    OnCallbackQuery,
    OnCommand,
    OnConnect,
    OnDisconnect,
    OnEditedMessage,
    OnError,
    OnEvent,
    OnMessage,
    OnPreCheckoutQuery,
    OnShippingQuery,
    OnInitialize,
    OnShutdown,
    OnUpdate,
    RemoveEventHandler
):
    pass
