from ...objects import Message


class SendVoice:

    async def send_voice(self, chat_id, voice, caption=None, duration=None, reply_to_message_id=None):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendVoice", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
