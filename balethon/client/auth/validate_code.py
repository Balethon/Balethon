import balethon
try:
    from balethon.proto import requests, structs, responses
except ImportError:
    pass


class ValidateCode:

    async def validate_code(
            self: "balethon.Client",
            transaction_hash: str,
            code: str,
            is_jwt: bool = True
    ) -> "responses.Auth":
        is_jwt = structs.BoolValue(value=is_jwt)
        kwargs = locals()
        del kwargs["self"]
        response = await self.execute(requests.ValidateCode(**kwargs))
        result = responses.Auth()
        result.ParseFromString(response)
        return result
