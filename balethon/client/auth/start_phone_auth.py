import uuid

import balethon
from balethon.proto import request_pb2, response_pb2


class StartPhoneAuth:

    async def start_phone_auth(
            self: "balethon.Client",
            phone_number: str,
            app_id: int = 4,
            api_key: str = "C28D46DC4C3A7A26564BFCC48B929086A95C93C98E789A19847BEE8627DE4E7D",
            device_hash: str = None,
            device_title: str = "Chrome_137.0.0.0, Windows",
            send_code_type: int = 1
    ) -> response_pb2.StartPhoneAuth:
        if device_hash is None:
            device_hash = str(uuid.uuid4())
        phone_number = int(phone_number)
        kwargs = locals()
        del kwargs["self"]
        start_phone_auth = request_pb2.StartPhoneAuth(**kwargs)
        response = await self.http2_connection.request(
            service="bale.auth.v1.Auth/StartPhoneAuth",
            content=start_phone_auth.SerializeToString()
        )
        result = response_pb2.StartPhoneAuth()
        result.ParseFromString(response)
        return result
