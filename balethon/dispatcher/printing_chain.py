from traceback import print_exception

from .chain import Chain


class PrintingChain(Chain):

    def __init__(self, name=None, condition=None):
        super().__init__(name or __name__, condition)

    @Chain.error_handler()
    def print_error(self, error):
        print_exception(None, error, error.__traceback__)

    @Chain.initialize_handler()
    def print_ready(self, client):
        print(f"---{client} is ready---")

    @Chain.shutdown_handler()
    def print_stopped(self, client):
        print(f"---{client} has stopped---")
