from network import Connection


class Client:

    def __init__(self, token):
        self.token = token
        self.connection = None

    @property
    def url(self):
        return f"https://tapi.bale.ai/bot{self.token}"

    async def connect(self):
        self.connection = Connection(self.token)
        await self.connection.start()

    async def disconnect(self):
        await self.connection.stop()
        self.connection = None

    # messages
    async def send_message(self, chat_id, text, reply_markup=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "text": text, "reply_markup": reply_markup, "reply_to_message_id": reply_to_message_id}
        async with self.connection.execute("post", "sendMessage", json) as response:
            return await response.json()

    # messages
    async def edit_message_text(self, chat_id, message_id, text):
        json = {"chat_id": chat_id, "message_id": message_id, "text": text}
        async with self.connection.execute("post", "editMessageText", json) as response:
            return await response.json()

    # messages
    async def delete_message(self, chat_id, message_id):
        json = {"chat_id": chat_id, "message_id": message_id}
        async with self.connection.execute("get", "deleteMessage", json) as response:
            return await response.json()

    # updates
    async def get_updates(self, offset=0, limit=0):
        json = {"offset": offset, "limit": limit}
        async with self.connection.execute("post", "getUpdates", json) as response:
            return await response.json()

    # updates
    async def set_webhook(self, url):
        json = {"url": url}
        async with self.connection.execute("post", "setWebhook", json) as response:
            return await response.json()

    # updates
    async def delete_webhook(self):
        async with self.connection.execute("get", "deleteWebhook") as response:
            return await response.json()

    # users
    async def get_me(self):
        async with self.connection.execute("get", "getMe") as response:
            return await response.json()

    # attachments
    async def send_photo(self, chat_id, photo, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "photo": photo, "caption": caption, "reply_to_message_id": reply_to_message_id}
        async with self.connection.execute("post", "sendPhoto", json) as response:
            return await response.json()

    # attachments
    async def send_audio(self, chat_id, audio, caption=0, duration=0, title=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "audio": audio, "caption": caption, "duration": duration, "title": title, "reply_to_message_id": reply_to_message_id}
        async with self.connection.execute("post", "sendAudio", json) as response:
            return await response.json()

    # attachments
    async def send_document(self, chat_id, document, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "document": document, "caption": caption, "reply_to_message_id": reply_to_message_id}
        async with self.connection.execute("post", "sendDocument", json) as response:
            return await response.json()

    # attachments
    async def send_video(self, chat_id, video, duration=0, width=0, height=0, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "video": video, "duration": duration, "width": width, "height": height, "caption": caption, "reply_to_message_id": reply_to_message_id}
        async with self.connection.execute("post", "sendVideo", json) as response:
            return await response.json()

    # attachments
    async def send_voice(self, chat_id, voice, caption=0, duration=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "voice": voice, "caption": caption, "duration": duration, "reply_to_message_id": reply_to_message_id}
        async with self.connection.execute("post", "sendVoice", json) as response:
            return await response.json()

    # attachments
    async def send_location(self, chat_id, latitude, longitude, reply_to_message_id=0):
        json = {"chat_id": chat_id, "latitude": latitude, "longitude": longitude, "reply_to_message_id": reply_to_message_id}
        async with self.connection.execute("post", "sendLocation", json) as response:
            return await response.json()

    # attachments
    async def send_contact(self, chat_id, phone_number, first_name, last_name=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "phone_number": phone_number, "first_name": first_name, "last_name": last_name, "reply_to_message_id": reply_to_message_id}
        async with self.connection.execute("post", "sendContact", json) as response:
            return await response.json()

    # attachments
    async def get_file(self, file_id):
        json = {"file_id": file_id}
        async with self.connection.execute("get", "getFile", json) as response:
            return await response.json()

    # chats
    async def get_chat(self, chat_id):
        json = {"chat_id": chat_id}
        async with self.connection.execute("get", "getChat", json) as response:
            return await response.json()

    # chats
    async def get_chat_administrators(self, chat_id):
        json = {"chat_id": chat_id}
        async with self.connection.execute("get", "getChatAdministrators", json) as response:
            return await response.json()

    # chats
    async def get_chat_members_count(self, chat_id):
        json = {"chat_id": chat_id}
        async with self.connection.execute("get", "getChatMembersCount", json) as response:
            return await response.json()

    # chats
    async def get_chat_member(self, chat_id, user_id):
        json = {"chat_id": chat_id, "user_id": user_id}
        async with self.connection.execute("get", "getChatMember", json) as response:
            return await response.json()

    # payments
    async def send_invoice(self, chat_id, title, description, provider_token, prices):
        json = {"chat_id": chat_id, "title": title, "description": description, "provider_token": provider_token, "prices": prices}
        async with self.connection.execute("post", "sendInvoice", json) as response:
            return await response.json()

    async def polling(self, callback):
        seen = [u["message"]["message_id"] for u in (await self.get_updates())["result"] if u.get("message")]
        while True:
            updates = (await self.get_updates())["result"]
            print(updates)
            for update in updates:
                if "message" not in update.keys():
                    continue
                message = update["message"]
                if message["message_id"] in seen:
                    continue
                seen.append(message["message_id"])
                await callback(self, message)
