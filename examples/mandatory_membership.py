from balethon import Client
from balethon.conditions import is_joined

bot = Client("TOKEN")

CHAT_ID = 1234567890


@bot.on_message(~is_joined(CHAT_ID))
async def not_joined(message):
    await message.reply("Please join our chat first")


@bot.on_message()
async def answer_message(message):
    await message.reply("Thank you for using this bot")


bot.run()
