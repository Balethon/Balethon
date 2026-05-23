import uuid

import balethon
try:
    from balethon.proto import requests, responses
except ImportError:
    pass


class StartPhoneAuth:

    async def start_phone_auth(
            self: "balethon.Client",
            phone_number: str,
            app_id: int = 4,
            api_key: str = "C28D46DC4C3A7A26564BFCC48B929086A95C93C98E789A19847BEE8627DE4E7D",
            device_hash: str = None,
            device_title: str = "Chrome_137.0.0.0, Windows",
            send_code_type: int = 1
    ) -> "responses.StartPhoneAuth":
        if device_hash is None:
            device_hash = str(uuid.uuid4())
        phone_number = int(phone_number)
        kwargs = locals()
        del kwargs["self"]
        return await self.execute(requests.StartPhoneAuth(**kwargs))
