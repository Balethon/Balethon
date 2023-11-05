from .rpc_error import RPCError


class NotFoundError(RPCError):
    name = "Not Found"
    code = 404
