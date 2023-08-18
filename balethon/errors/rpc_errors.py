class RPCError(Exception):
    name = "RPC"
    code = None

    @classmethod
    def create(cls, code, description):
        for rpc_error in cls.__subclasses__():
            if code == rpc_error.code:
                return rpc_error(description)
        return cls(description, code)

    def __init__(self, description, code=None):
        self.description = description
        self.code = code or self.code

    def __str__(self):
        code = "" if self.code is None else f" {self.code}"
        description = "" if self.description is None else f" - {self.description}"
        return f"({self.name}{code}){description}"


class BadRequestError(RPCError):
    name = "Bad Request"
    code = 400


class UnauthorizedError(RPCError):
    name = "Unauthorized"
    code = 401


class ForbiddenError(RPCError):
    name = "Forbidden"
    code = 403


class NotFoundError(RPCError):
    name = "Not Found"
    code = 404


class FloodError(RPCError):
    name = "Flood"
    code = 420


class InternalError(RPCError):
    name = "Internal"
    code = 500
