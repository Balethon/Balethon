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
        sign_up = requests.SignUp(**kwargs)
        response = await self.http2_connection.request(
            service="bale.auth.v1.Auth/SignUp",
            content=sign_up.SerializeToString()
        )
        result = responses.Auth()
        result.ParseFromString(response)
        return result
