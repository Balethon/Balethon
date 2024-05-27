class RPCError(Exception):
    name = "RPC Error"
    code = None

    @classmethod
    def create(cls, code: int = None, description: str = None, reason: str = None, parameters: dict = None):
        for rpc_error in cls.__subclasses__():
            if code == rpc_error.code:
                return rpc_error(code, description, reason, parameters)
        return cls(code, description, reason, parameters)

    def __init__(self, code: int = None, description: str = None, reason: str = None, parameters: dict = None):
        self.code = code or self.code
        self.description = description
        self.reason = reason
        self.parameters = parameters
        super().__init__(str(self))

    def __str__(self):
        code = "" if self.code is None else f" {self.code}"
        description = "" if self.description is None else f": {self.description}"
        reason = "" if self.reason is None else f" (caused by {self.reason})"
        return f"{self.name}{code}{description}{reason}"
