from .rpc_error import RPCError


class InternalError(RPCError):
    name = "Internal"
    code = 500
