import balethon
from balethon.proto import request_pb2, struct_pb2, response_pb2


class SignUp:

    async def sign_up(
            self: "balethon.Client",
            transaction_hash: str,
            name: str,
            password: str = None
    ) -> response_pb2.Auth:
        password = struct_pb2.StringValue(value=password)
        kwargs = locals()
        del kwargs["self"]
        sign_up = request_pb2.SignUp(**kwargs)
        response = await self.http2_connection.request(
            service="bale.auth.v1.Auth/SignUp",
            content=sign_up.SerializeToString()
        )
        result = response_pb2.Auth()
        result.ParseFromString(response)
        return result
