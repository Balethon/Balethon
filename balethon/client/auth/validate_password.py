import balethon
from balethon.proto import request_pb2, struct_pb2, response_pb2


class ValidatePassword:

    async def validate_password(
            self: "balethon.Client",
            transaction_hash: str,
            code: str,
            is_jwt: bool = True
    ) -> response_pb2.Auth:
        is_jwt = struct_pb2.BoolValue(value=is_jwt)
        kwargs = locals()
        del kwargs["self"]
        validate_password = request_pb2.ValidatePassword(**kwargs)
        response = await self.http2_connection.request(
            service="bale.auth.v1.Auth/ValidatePassword",
            content=validate_password.SerializeToString()
        )
        result = response_pb2.Auth()
        result.ParseFromString(response)
        return result
