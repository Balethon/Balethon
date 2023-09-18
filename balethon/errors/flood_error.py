from .rpc_error import RPCError


class FloodError(RPCError):
    name = "Flood"
    code = 420
