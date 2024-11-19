from sys import stdout

from .chain import Chain


class MonitoringChain(Chain):

    def __init__(self, name=None, condition=None, stream=None):
        super().__init__(name or __name__, condition)
        self.stream = stream or stdout

    @Chain.message_handler()
    def monitor_message(self, message):
        self.stream.write(f"{message.author.full_name}: {message.content}\n")

    @Chain.callback_query_handler()
    def monitor_callback_query(self, callback_query):
        self.stream.write(f"{callback_query.author.full_name}: [{callback_query.data}]\n")
