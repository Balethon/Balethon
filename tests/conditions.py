from balethon import Client
from balethon import conditions

import config

bot = Client(config.TOKEN)


@bot.on_message()
async def main(_, message):
    print(f"{message.author.full_name}: {message.text}")


@bot.on_message(conditions.all, "all")
async def test_all(_, __):
    print("This message falls under the condition of ALL")


@bot.on_message(conditions.forward, "forward")
async def test_forward(_, __):
    print("This message falls under the condition of FORWARD")


@bot.on_message(conditions.reply, "reply")
async def test_reply(_, __):
    print("This message falls under the condition of REPLY")


@bot.on_message(conditions.text, "text")
async def test_text(_, __):
    print("This message falls under the condition of TEXT")


@bot.on_message(conditions.entities, "entities")
async def test_entities(_, __):
    print("This message falls under the condition of ENTITIES")


@bot.on_message(conditions.document, "document")
async def test_document(_, __):
    print("This message falls under the condition of DOCUMENT")


@bot.on_message(conditions.photo, "photo")
async def test_photo(_, __):
    print("This message falls under the condition of PHOTO")


@bot.on_message(conditions.video, "video")
async def test_video(_, __):
    print("This message falls under the condition of VIDEO")


@bot.on_message(conditions.voice, "voice")
async def test_voice(_, __):
    print("This message falls under the condition of VOICE")


@bot.on_message(conditions.caption, "caption")
async def test_caption(_, __):
    print("This message falls under the condition of CAPTION")


@bot.on_message(conditions.contact, "contact")
async def test_contact(_, __):
    print("This message falls under the condition of CONTACT")


@bot.on_message(conditions.location, "location")
async def test_location(_, __):
    print("This message falls under the condition of LOCATION")


@bot.on_message(conditions.new_chat_members, "new_chat_members")
async def test_new_chat_members(_, __):
    print("This message falls under the condition of NEW CHAT MEMBERS")


@bot.on_message(conditions.left_chat_member, "left_chat_member")
async def test_left_chat_member(_, __):
    print("This message falls under the condition of LEFT CHAT MEMBER")


@bot.on_message(conditions.new_chat_title, "new_chat_title")
async def test_new_chat_title(_, __):
    print("This message falls under the condition of NEW CHAT TITLE")


@bot.on_message(conditions.new_chat_photo, "new_chat_photo")
async def test_new_chat_photo(_, __):
    print("This message falls under the condition of NEW CHAT PHOTO")


@bot.on_message(conditions.delete_chat_photo, "delete_chat_photo")
async def test_delete_chat_photo(_, __):
    print("This message falls under the condition of DELETE CHAT PHOTO")


@bot.on_message(conditions.group_chat_created, "group_chat_created")
async def test_group_chat_created(_, __):
    print("This message falls under the condition of GROUP CHAT CREATED")


@bot.on_message(conditions.supergroup_chat_created, "supergroup_chat_created")
async def test_supergroup_chat_created(_, __):
    print("This message falls under the condition of SUPERGROUP CHAT CREATED")


@bot.on_message(conditions.channel_chat_created, "channel_chat_created")
async def test_channel_chat_created(_, __):
    print("This message falls under the condition of CHANNEL CHAT CREATED")


@bot.on_message(conditions.pinned_message, "pinned_message")
async def test_pinned_message(_, __):
    print("This message falls under the condition of PINNED MESSAGE")


@bot.on_message(conditions.invoice, "invoice")
async def test_invoice(_, __):
    print("This message falls under the condition of INVOICE")


@bot.on_message(conditions.media, "media")
async def test_media(_, __):
    print("This message falls under the condition of MEDIA")


@bot.on_message(conditions.command("command"), "command")
async def test_command(_, __):
    print("This message falls under the condition of COMMAND")


@bot.on_message(conditions.private, "private")
async def test_private(_, __):
    print("This message falls under the condition of PRIVATE")


@bot.on_message(conditions.regex("test"), "regex")
async def test_private(_, __):
    print("This message falls under the condition of REGEX")


@bot.on_message(conditions.chat(int(config.USER_ID)), "chat")
async def test_chat(_, __):
    print("This message falls under the condition of CHAT")


@bot.on_message(conditions.is_joined(config.CHAT_ID), "is_joined")
async def test_is_joined(_, __):
    print("This message falls under the condition of IS JOINED")


if __name__ == "__main__":
    bot.run()
