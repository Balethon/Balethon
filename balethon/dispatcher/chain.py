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

    def to_string(self, keyword="if", tabs=0):
        result = []
        if self.condition:
            result.append(f"{'    ' * tabs}{keyword} {self.condition}:")
            tabs += 1
        for i, child in enumerate(self.children):
            if i:
                keyword = "elif"
            elif not self.condition:
                keyword = keyword
            else:
                keyword = "if"
            result.append(child.to_string(keyword, tabs))
        for i, child in enumerate(self.chains):
            result.append(child.to_string("elif" if i else "if", tabs))
        return "\n".join(result)

    def __repr__(self):
        return self.to_string()

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
        self.children.append(event_handler)

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
