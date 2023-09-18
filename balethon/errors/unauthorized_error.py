from .rpc_error import RPCError


class UnauthorizedError(RPCError):
    name = "Unauthorized"
    code = 401
