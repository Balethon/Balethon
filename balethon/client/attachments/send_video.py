from ...objects import Message


class SendVideo:

    async def send_video(self, chat_id, video, duration=None, width=None, height=None, caption=None, reply_to_message_id=None):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendVideo", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
