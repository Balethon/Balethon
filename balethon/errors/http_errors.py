from .rpc_error import RPCError


class HTTPError(RPCError):
    name = "HTTP Error"


class BadRequestError(HTTPError):
    name = "Bad Request"
    code = 400


class UnauthorizedError(HTTPError):
    name = "Unauthorized"
    code = 401


class ForbiddenError(HTTPError):
    name = "Forbidden"
    code = 403


class NotFoundError(HTTPError):
    name = "Not Found"
    code = 404


class FloodError(HTTPError):
    name = "Flood"
    code = 420


class TooManyRequestsError(HTTPError):
    name = "Too Many Requests"
    code = 429

    def __init__(self, code: int = None, description: str = None, reason: str = None, parameters: dict = None):
        super().__init__(code, description, reason, parameters)
        self.seconds = parameters.get("retry_after", 0)


class InternalError(HTTPError):
    name = "Internal"
    code = 500
