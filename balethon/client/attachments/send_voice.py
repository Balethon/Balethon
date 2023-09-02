class SendVoice:

    async def send_voice(self, chat_id, voice, caption=None, duration=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "voice": voice, "caption": caption, "duration": duration, "reply_to_message_id": reply_to_message_id}
        return await self.connection.execute("post", "sendVoice", json)
