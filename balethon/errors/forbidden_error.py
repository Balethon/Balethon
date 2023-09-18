from .rpc_error import RPCError


class ForbiddenError(RPCError):
    name = "Forbidden"
    code = 403
