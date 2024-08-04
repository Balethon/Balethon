from balethon import Client
from balethon.conditions import new_chat_members

bot = Client("TOKEN")


@bot.on_message(new_chat_members)
async def welcome_new_chat_members(message):
    members = ", ".join(str(member) for member in message.new_chat_members)
    await message.reply(
        f"Hello {members}, welcome to {message.chat}!"
    )


bot.run()
