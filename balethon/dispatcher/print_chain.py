from traceback import print_exception

from .chain import Chain

print_chain = Chain()


@print_chain.on_error()
def print_error(error):
    print_exception(None, error, error.__traceback__)


@print_chain.on_initialize()
def print_ready(client):
    print(f"---{client} is ready---")


@print_chain.on_shutdown()
def print_stopped(client):
    print(f"---{client} has stopped---")
