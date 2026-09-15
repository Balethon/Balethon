from .rpc_error import RPCError


class GRPCError(RPCError):
    name = "GRPC Error"


class InvalidArgument(GRPCError):
    name = "Invalid Argument"
    code = 3


class PermissionDenied(GRPCError):
    name = "Permission Denied"
    code = 7


class ResourceExhausted(GRPCError):
    name = "Resource Exhausted"
    code = 8
