from ...objects import Message


class SendAudio:

    async def send_audio(self, chat_id, audio, caption=None, duration=None, title=None, reply_to_message_id=None):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendAudio", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
