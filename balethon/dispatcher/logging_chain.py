from logging import getLogger

from .chain import Chain


class LoggingChain(Chain):

    def __init__(self, name=None, condition=None, logger=None):
        super().__init__(name or __name__, condition)
        self.log = logger or getLogger(self.name)

    @Chain.error_handler()
    def log_error(self, error):
        self.log.exception(error)

    @Chain.connect_handler()
    def log_connect(self, client):
        self.log.info(f"{client} connected")

    @Chain.initialize_handler()
    def log_initialize(self, client):
        sync_workers = client.dispatcher.sync_workers_count
        async_workers = client.dispatcher.async_workers_count
        self.log.info(f"{client} initialized (sync workers: {sync_workers} - async workers: {async_workers})")

    @Chain.shutdown_handler()
    def log_shutdown(self, client):
        self.log.info(f"{client} shutting down")

    @Chain.disconnect_handler()
    def log_disconnect(self, client):
        self.log.info(f"{client} disconnected")

    @Chain.event_handler()
    def log_event(self, event):
        self.log.info(event)
