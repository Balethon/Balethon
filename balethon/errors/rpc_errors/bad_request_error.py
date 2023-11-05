from .rpc_error import RPCError


class BadRequestError(RPCError):
    name = "Bad Request"
    code = 400
