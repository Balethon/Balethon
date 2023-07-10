from .bale_error import BaleError


class RPCError(BaleError):

    def __init__(self):
        pass


class BadRequestError(RPCError):
    code = 400


class UnauthorizedError(RPCError):
    code = 401


class ForbiddenError(RPCError):
    code = 403


class NotFoundError(RPCError):
    code = 404


class FloodError(RPCError):
    code = 420


class InternalError(RPCError):
    code = 500
