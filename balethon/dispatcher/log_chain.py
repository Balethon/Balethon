from logging import getLogger

from .chain import Chain

log = getLogger(__name__)

log_chain = Chain("log")


@log_chain.on_error()
def log_error(error):
    log.exception(error)


@log_chain.on_connect()
def log_connect(client):
    log.info(f"{client} connected")


@log_chain.on_initialize()
def log_initialize(client):
    log.info(f"{client} initialized")


@log_chain.on_shutdown()
def log_shutdown(client):
    log.info(f"{client} shutting down")


@log_chain.on_disconnect()
def log_disconnect(client):
    log.info(f"{client} disconnected")


@log_chain.on_event()
def log_event(event):
    log.info(event)
