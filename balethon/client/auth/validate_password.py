import balethon
try:
    from balethon.proto import requests, structs, responses
except ImportError:
    pass


class ValidatePassword:

    async def validate_password(
            self: "balethon.Client",
            transaction_hash: str,
            code: str,
            is_jwt: bool = True
    ) -> "responses.Auth":
        is_jwt = structs.BoolValue(value=is_jwt)
        kwargs = locals()
        del kwargs["self"]
        response = await self.execute(requests.ValidatePassword(**kwargs))
        result = responses.Auth()
        result.ParseFromString(response)
        return result
