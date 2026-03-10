import balethon
from balethon.network import HTTP2Connection
from balethon.proto import request_pb2, struct_pb2, response_pb2


class ValidateCode:

    async def validate_code(
            self: "balethon.Client",
            transaction_hash: str,
            code: str,
            is_jwt: bool = True
    ) -> response_pb2.Auth:
        is_jwt = struct_pb2.BoolValue(value=is_jwt)
        kwargs = locals()
        del kwargs["self"]
        validate_code = request_pb2.ValidateCode(**kwargs)
        connection = HTTP2Connection()
        response = await connection.request(
            "POST",
            service="bale.auth.v1.Auth/ValidateCode",
            content=validate_code.SerializeToString()
        )
        result = response_pb2.Auth()
        result.ParseFromString(response)
        return result
