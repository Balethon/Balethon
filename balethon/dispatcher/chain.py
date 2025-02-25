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

    def __init__(self, name, condition=None, *chains):
        self.name = name
        self.condition = condition
        self.chains = list(chains)
        self.children = []
        for attribute_name in dir(self):
            attribute = getattr(self, attribute_name)
            if isinstance(attribute, EventHandler):
                attribute.self = self
                self.add_event_handler(attribute)

    async def check(self, client, event):
        if self.condition is None:
            return True
        return await self.condition(client, event)

    @staticmethod
    def create_event_handler(event_handler, *args, **kwargs):
        def decorator(callback):
            return event_handler(callback, *args, **kwargs)
        return decorator

    def add_event_handler(self, event_handler, *args, **kwargs):
        if isinstance(event_handler, type):
            def decorator(callback):
                event_handler_instance = event_handler(callback, *args, **kwargs)
                self.add_event_handler(event_handler_instance)
                return event_handler_instance
            return decorator
        self.children.append(event_handler)

    @classmethod
    def connect_handler(cls):
        return cls.create_event_handler(ConnectHandler)

    def on_connect(self):
        return self.add_event_handler(ConnectHandler)

    @classmethod
    def initialize_handler(cls):
        return cls.create_event_handler(InitializeHandler)

    def on_initialize(self):
        return self.add_event_handler(InitializeHandler)

    @classmethod
    def event_handler(cls, condition=None):
        return cls.create_event_handler(EventHandler, condition)

    def on_event(self, condition=None):
        return self.add_event_handler(EventHandler, condition)

    @classmethod
    def error_handler(cls, condition=None):
        return cls.create_event_handler(ErrorHandler, condition)

    def on_error(self, condition=None):
        return self.add_event_handler(ErrorHandler, condition)

    @classmethod
    def update_handler(cls, condition=None):
        return cls.create_event_handler(UpdateHandler, condition)

    def on_update(self, condition=None):
        return self.add_event_handler(UpdateHandler, condition)

    @classmethod
    def message_handler(cls, condition=None):
        return cls.create_event_handler(MessageHandler, condition)

    def on_message(self, condition=None):
        return self.add_event_handler(MessageHandler, condition)

    @classmethod
    def edited_message_handler(cls, condition=None):
        return cls.create_event_handler(EditedMessageHandler, condition)

    def on_edited_message(self, condition=None):
        return self.add_event_handler(EditedMessageHandler, condition)

    @classmethod
    def command_handler(cls, condition=None, name=None, min_arguments=None, max_arguments=None):
        return cls.create_event_handler(CommandHandler, condition, name, min_arguments, max_arguments)

    def on_command(self, condition=None, name=None, min_arguments=None, max_arguments=None):
        return self.add_event_handler(CommandHandler, condition, name, min_arguments, max_arguments)

    @classmethod
    def callback_query_handler(cls, condition=None):
        return cls.create_event_handler(CallbackQueryHandler, condition)

    def on_callback_query(self, condition=None):
        return self.add_event_handler(CallbackQueryHandler, condition)

    @classmethod
    def pre_checkout_query_handler(cls, condition=None):
        return cls.create_event_handler(PreCheckoutQueryHandler, condition)

    def on_pre_checkout_query(self, condition=None):
        return self.add_event_handler(PreCheckoutQueryHandler, condition)

    @classmethod
    def shipping_query_handler(cls, condition=None):
        return cls.create_event_handler(ShippingQueryHandler, condition)

    def on_shipping_query(self, condition=None):
        return self.add_event_handler(ShippingQueryHandler, condition)

    @classmethod
    def shutdown_handler(cls):
        return cls.create_event_handler(ShutdownHandler)

    def on_shutdown(self):
        return self.add_event_handler(ShutdownHandler)

    @classmethod
    def disconnect_handler(cls):
        return cls.create_event_handler(DisconnectHandler)

    def on_disconnect(self):
        return self.add_event_handler(DisconnectHandler)

    def remove_event_handler(self, event_handler):
        self.children.remove(event_handler)

    def add(self, *chains):
        self.children.extend(chains)

    def include(self, *chains):
        self.chains.extend(chains)

    def get(self, name):
        for chain in self.chains:
            if chain.name == name:
                return chain
        raise ValueError(f"Chain \"{name}\" does not exist")

    def delete(self, name):
        for i, c in enumerate(self.chains):
            if c.name == name:
                del self.chains[i]
                return
        for i, c in enumerate(self.children):
            if isinstance(c, Chain) and c.name == name:
                del self.children[i]
                return
        raise ValueError(f"Chain \"{name}\" does not exist")
