import balethon
try:
    from balethon.proto import requests, structs, responses
except ImportError:
    pass


class ValidatePassword:

    async def validate_password(
            self: "balethon.Client",
            transaction_hash: str,
            password: str,
            is_jwt: bool = True
    ) -> "responses.Auth":
        request = requests.ValidatePassword(
            transaction_hash=transaction_hash,
            code=password,
            is_jwt=structs.BoolValue(value=is_jwt),
        )
        response = await self.execute(request)
        result = responses.Auth()
        result.ParseFromString(response)
        return result
