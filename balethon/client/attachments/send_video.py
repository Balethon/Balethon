from ...objects import Message


class SendVideo:

    async def send_video(self, chat_id, video, duration=None, width=None, height=None, caption=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "video": video, "duration": duration, "width": width, "height": height, "caption": caption, "reply_to_message_id": reply_to_message_id}
        result = await self.connection.execute("post", "sendVideo", json)
        return Message.wrap(result)
