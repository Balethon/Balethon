import balethon
try:
    from balethon.proto import request_pb2, struct_pb2, response_pb2
except ImportError:
    pass


class ValidateCode:

    async def validate_code(
            self: "balethon.Client",
            transaction_hash: str,
            code: str,
            is_jwt: bool = True
    ) -> "response_pb2.Auth":
        is_jwt = struct_pb2.BoolValue(value=is_jwt)
        kwargs = locals()
        del kwargs["self"]
        validate_code = request_pb2.ValidateCode(**kwargs)
        response = await self.http2_connection.request(
            service="bale.auth.v1.Auth/ValidateCode",
            content=validate_code.SerializeToString()
        )
        result = response_pb2.Auth()
        result.ParseFromString(response)
        return result
