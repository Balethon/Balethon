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
        validate_password = requests.ValidatePassword(**kwargs)
        response = await self.http2_connection.request(
            service="bale.auth.v1.Auth/ValidatePassword",
            content=validate_password.SerializeToString()
        )
        result = responses.Auth()
        result.ParseFromString(response)
        return result
