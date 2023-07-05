from aiohttp import ClientSession

#Abolam
class Client:

    def __init__(self, token):
        self.token = token
        self.session = None

    @property
    def url(self):
        return f"https://tapi.bale.ai/bot{self.token}"

    async def connect(self):
        self.session = ClientSession()

    async def disconnect(self):
        self.session.close()
        self.session = None

    # messages
    async def send_message(self, chat_id, text):
        params = {"chat_id": chat_id, "text": text}
        async with self.session.post(f"{self.url}/sendMessage", params=params) as response:
            return await response.json()

    # messages
    async def edit_message_text(self, chat_id, message_id, text):
        params = {"chat_id": chat_id, "message_id": message_id, "text": text}
        async with self.session.post(f"{self.url}/editMessageText", params=params) as response:
            return await response.json()

    # messages
    async def delete_message(self, chat_id, message_id):
        params = {"chat_id": chat_id, "message_id": message_id}
        async with self.session.get(f"{self.url}/deleteMessage", params=params) as response:
            return await response.json()

    # updates
    async def get_updates(self):
        async with self.session.post(f"{self.url}/getUpdates") as response:
            return await response.json()

    # updates
    async def set_webhook(self, url):
        params = {"url": url}
        async with self.session.post(f"{self.url}/setWebhook", params=params) as response:
            return await response.json()

    # updates
    async def delete_webhook(self):
        async with self.session.get(f"{self.url}/deleteWebhook") as response:
            return await response.json()

    # users
    async def get_me(self):
        async with self.session.get(f"{self.url}/getMe") as response:
            return await response.json()

    # chats
    async def get_chat(self, chat_id):
        params = {"chat_id": chat_id}
        async with self.session.get(f"{self.url}/getChat", params=params) as response:
            return await response.json()

    # chats
    async def get_chat_administrators(self, chat_id):
        params = {"chat_id": chat_id}
        async with self.session.get(f"{self.url}/getChatAdministrators", params=params) as response:
            return await response.json()

    # chats
    async def get_chat_members_count(self, chat_id):
        params = {"chat_id": chat_id}
        async with self.session.get(f"{self.url}/getChatMembersCount", params=params) as response:
            return await response.json()

    # chats
    async def get_chat_member(self, chat_id, user_id):
        params = {"chat_id": chat_id, "user_id": user_id}
        async with self.session.get(f"{self.url}/getChatMember", params=params) as response:
            return await response.json()

    # payments
    async def send_invoice(self, chat_id, title, description, provider_token, prices):
        params = {"chat_id": chat_id, "title": title, "description": description, "provider_token": provider_token, "prices": prices}
        async with self.session.get(f"{self.url}/sendInvoice", params=params) as response:
            return await response.json()
