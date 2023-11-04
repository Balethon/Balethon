import balethon
from ...event_handlers import UpdateHandler


class OnUpdate:

    def on_update(
            self: "balethon.Client",
            condition=None,
            chain="default"
    ):
        return self.add_event_handler(UpdateHandler, chain, condition)
