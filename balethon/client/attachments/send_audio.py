from ...objects import Message


class SendAudio:

    async def send_audio(self, chat_id, audio, caption=None, duration=None, title=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "audio": audio, "caption": caption, "duration": duration, "title": title, "reply_to_message_id": reply_to_message_id}
        result = await self.connection.execute("post", "sendAudio", json)
        return Message.wrap(result)
