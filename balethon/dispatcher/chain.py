from ..event_handlers import (
    ConnectHandler,
    InitializeHandler,
    EventHandler,
    ErrorHandler,
    UpdateHandler,
    MessageHandler,
    EditedMessageHandler,
    CommandHandler,
    CallbackQueryHandler,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
    ShutdownHandler,
    DisconnectHandler
)


class Chain:

    def __init__(self, name, condition=None):
        self.name = name
        self.condition = condition
        self.event_handlers = []

    def __repr__(self):
        event_handlers = ", ".join(repr(event_handler) for event_handler in self.event_handlers)
        return f"Chain({event_handlers})"

    async def check(self, client, event):
        if self.condition is None:
            return True
        return await self.condition(client, event)

    def add_event_handler(self, event_handler, *args, **kwargs):
        if isinstance(event_handler, type):
            def decorator(callback):
                self.add_event_handler(event_handler(callback, *args, **kwargs))
                return callback
            return decorator
        self.event_handlers.append(event_handler)

    def on_connect(self):
        return self.add_event_handler(ConnectHandler)

    def on_initialize(self):
        return self.add_event_handler(InitializeHandler)

    def on_event(self, condition=None):
        return self.add_event_handler(EventHandler, condition)

    def on_error(self, condition=None):
        return self.add_event_handler(ErrorHandler, condition)

    def on_update(self, condition=None):
        return self.add_event_handler(UpdateHandler, condition)

    def on_message(self, condition=None):
        return self.add_event_handler(MessageHandler, condition)

    def on_edited_message(self, condition=None):
        return self.add_event_handler(EditedMessageHandler, condition)

    def on_command(self, condition=None, name=None, min_arguments=None, max_arguments=None):
        return self.add_event_handler(CommandHandler, condition, name, min_arguments, max_arguments)

    def on_callback_query(self, condition=None):
        return self.add_event_handler(CallbackQueryHandler, condition)

    def on_pre_checkout_query(self, condition=None):
        return self.add_event_handler(PreCheckoutQueryHandler, condition)

    def on_shipping_query(self, condition=None):
        return self.add_event_handler(ShippingQueryHandler, condition)

    def on_shutdown(self):
        return self.add_event_handler(ShutdownHandler)

    def on_disconnect(self):
        return self.add_event_handler(DisconnectHandler)

    def remove_event_handler(self, event_handler):
        self.event_handlers.remove(event_handler)

    def include(self, other):
        self.event_handlers.extend(other.event_handlers)
