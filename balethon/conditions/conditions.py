# TODO: separating the Conditions
from . import Condition


@Condition
async def all(condition, client, message):
    return True


@Condition
async def forward(condition, client, message):
    bool(message.forward_from or message.forward_from_chat)


@Condition
async def reply(condition, client, message):
    return bool(message.reply_to_message)


@Condition
async def text(condition, client, message):
    return bool(message.text)


@Condition
async def entities(condition, client, message):
    return bool(message.entities or message.caption_entities)


@Condition
async def document(condition, client, message):
    return bool(message.document)


@Condition
async def photo(condition, client, message):
    return bool(message.photo)


@Condition
async def video(condition, client, message):
    return bool(message.video)


@Condition
async def voice(condition, client, message):
    return bool(message.voice)


@Condition
async def caption(condition, client, message):
    return bool(message.caption)


@Condition
async def contact(condition, client, message):
    return bool(message.contact)


@Condition
async def location(condition, client, message):
    return bool(message.location)


@Condition
async def new_chat_members(condition, client, message):
    return bool(message.new_chat_members)


@Condition
async def left_chat_member(condition, client, message):
    return bool(message.left_chat_member)


@Condition
async def new_chat_title(condition, client, message):
    return bool(message.new_chat_title)


@Condition
async def new_chat_photo(condition, client, message):
    return bool(message.new_chat_photo)


@Condition
async def delete_chat_photo(condition, client, message):
    return bool(message.delete_chat_photo)


@Condition
async def group_chat_created(condition, client, message):
    return bool(message.group_chat_created)


@Condition
async def supergroup_chat_created(condition, client, message):
    return bool(message.supergroup_chat_created)


@Condition
async def channel_chat_created(condition, client, message):
    return bool(message.channel_chat_created)


@Condition
async def pinned_message(condition, client, message):
    return bool(message.pinned_message)


@Condition
async def invoice(condition, client, message):
    return bool(message.invoice)


@Condition
async def media(condition, client, message):
    return bool(
        message.photo or
        message.video or
        message.voice or
        message.document
    )


class Command(Condition):

    def __init__(self, name):
        super().__init__()
        self.name = name

    async def __call__(self, client, message):
        if not message.text.startswith("/"):
            return False
        if not message.text[1:].startswith(self.name):
            return False
        return True
