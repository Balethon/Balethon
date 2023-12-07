from .rpc_error import RPCError


class TooManyRequestsError(RPCError):
    name = "Too Many Requests"
    code = 429
