class RPCError(Exception):  # TODO: separating RPCErrors
    name = "RPC Error"
    code = None

    @classmethod
    def create(cls, code=None, description=None, reason=None):
        for rpc_error in cls.__subclasses__():
            if code == rpc_error.code:
                return rpc_error(code, description, reason)
        return cls(code, description, reason)

    def __init__(self, code=None, description=None, reason=None):
        self.code = code or self.code
        self.description = description
        self.reason = reason
        super().__init__(str(self))

    def __str__(self):
        code = "" if self.code is None else f" {self.code}"
        description = "" if self.description is None else f": {self.description}"
        reason = "" if self.reason is None else f" (caused by {self.reason})"
        return f"{self.name}{code}{description}{reason}"


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
