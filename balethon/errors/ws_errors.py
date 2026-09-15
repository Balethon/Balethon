from .rpc_error import RPCError


class WSError(RPCError):
    name = "WS Error"


class Unauthenticated(WSError):
    name = "Unauthenticated"
    code = 4401
