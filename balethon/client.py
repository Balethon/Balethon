from .network import Connection
from .dispatcher import Dispatcher
from .handlers import MessageHandler, CallbackQueryHandler


class Client:

    def __init__(self, token):
        self.token = token
        self.connection = None
        self.dispatcher = Dispatcher()

    async def connect(self):
        self.connection = Connection(self.token)
        await self.connection.start()

    async def disconnect(self):
        await self.connection.stop()
        self.connection = None

    def add_handler(self, handler):
        self.dispatcher.add_handler(handler)

    def remove_handler(self, handler):
        self.dispatcher.remove_handler(handler)

    def on_message(self, filters=None):
        def decorator(func):
            self.add_handler(MessageHandler(func))
            return func
        return decorator

    def on_callback_query(self, filters=None):
        def decorator(func):
            self.add_handler(CallbackQueryHandler(func))
            return func
        return decorator

    async def polling(self):
        seen = [u["update_id"] for u in (await self.get_updates())["result"]]
        while True:
            updates = (await self.get_updates())["result"]
            for update in updates:
                if update["update_id"] in seen:
                    continue
                seen.append(update["update_id"])
                await self.dispatcher(self, update)

    # messages
    async def send_message(self, chat_id, text, reply_markup=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "text": text, "reply_markup": reply_markup, "reply_to_message_id": reply_to_message_id}
        return await self.connection.execute("post", "sendMessage", json)

    # messages
    async def edit_message_text(self, chat_id, message_id, text, reply_markup=None):
        json = {"chat_id": chat_id, "message_id": message_id, "text": text, "reply_markup": reply_markup}
        return await self.connection.execute("post", "editMessageText", json)

    # messages
    async def delete_message(self, chat_id, message_id):
        json = {"chat_id": chat_id, "message_id": message_id}
        return await self.connection.execute("get", "deleteMessage", json)

    # updates
    async def get_updates(self, offset=0, limit=0):
        json = {"offset": offset, "limit": limit}
        return await self.connection.execute("post", "getUpdates", json)

    # updates
    async def set_webhook(self, url):
        json = {"url": url}
        return await self.connection.execute("post", "setWebhook", json)

    # updates
    async def delete_webhook(self):
        return await self.connection.execute("get", "deleteWebhook")

    # users
    async def get_me(self):
        return await self.connection.execute("get", "getMe")

    # attachments
    async def send_photo(self, chat_id, photo, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "photo": photo, "caption": caption, "reply_to_message_id": reply_to_message_id}
        return await self.connection.execute("post", "sendPhoto", json)

    # attachments
    async def send_audio(self, chat_id, audio, caption=0, duration=0, title=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "audio": audio, "caption": caption, "duration": duration, "title": title, "reply_to_message_id": reply_to_message_id}
        return await self.connection.execute("post", "sendAudio", json)

    # attachments
    async def send_document(self, chat_id, document, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "document": document, "caption": caption, "reply_to_message_id": reply_to_message_id}
        return await self.connection.execute("post", "sendDocument", json)

    # attachments
    async def send_video(self, chat_id, video, duration=0, width=0, height=0, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "video": video, "duration": duration, "width": width, "height": height, "caption": caption, "reply_to_message_id": reply_to_message_id}
        return await self.connection.execute("post", "sendVideo", json)

    # attachments
    async def send_voice(self, chat_id, voice, caption=0, duration=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "voice": voice, "caption": caption, "duration": duration, "reply_to_message_id": reply_to_message_id}
        return await self.connection.execute("post", "sendVoice", json)

    # attachments
    async def send_location(self, chat_id, latitude, longitude, reply_to_message_id=0):
        json = {"chat_id": chat_id, "latitude": latitude, "longitude": longitude, "reply_to_message_id": reply_to_message_id}
        return await self.connection.execute("post", "sendLocation", json)

    # attachments
    async def send_contact(self, chat_id, phone_number, first_name, last_name=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "phone_number": phone_number, "first_name": first_name, "last_name": last_name, "reply_to_message_id": reply_to_message_id}
        return await self.connection.execute("post", "sendContact", json)

    # attachments
    async def get_file(self, file_id):
        json = {"file_id": file_id}
        return await self.connection.execute("get", "getFile", json)

    # chats
    async def get_chat(self, chat_id):
        json = {"chat_id": chat_id}
        return await self.connection.execute("get", "getChat", json)

    # chats
    async def get_chat_administrators(self, chat_id):
        json = {"chat_id": chat_id}
        return await self.connection.execute("get", "getChatAdministrators", json)

    # chats
    async def get_chat_members_count(self, chat_id):
        json = {"chat_id": chat_id}
        return await self.connection.execute("get", "getChatMembersCount", json)

    # chats
    async def get_chat_member(self, chat_id, user_id):
        json = {"chat_id": chat_id, "user_id": user_id}
        return await self.connection.execute("get", "getChatMember", json)

    # payments
    async def send_invoice(self, chat_id, title, description, provider_token, prices):
        json = {"chat_id": chat_id, "title": title, "description": description, "provider_token": provider_token, "prices": prices}
        return await self.connection.execute("post", "sendInvoice", json)
