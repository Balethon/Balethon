from .rpc_error import RPCError


class TooManyRequestsError(RPCError):
    name = "Too Many Requests"
    code = 429

    def __init__(self, code: int = None, description: str = None, reason: str = None, parameters: dict = None):
        super().__init__(code, description, reason, parameters)
        self.seconds = parameters.get("retry_after", 0)
