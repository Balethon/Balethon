import balethon
try:
    from balethon.proto import requests, structs, responses
except ImportError:
    pass


class SignUp:

    async def sign_up(
            self: "balethon.Client",
            transaction_hash: str,
            name: str,
            password: str = None
    ) -> "responses.Auth":
        password = structs.StringValue(value=password)
        kwargs = locals()
        del kwargs["self"]
        response = await self.execute(requests.SignUp(**kwargs))
        result = responses.Auth()
        result.ParseFromString(response)
        return result
