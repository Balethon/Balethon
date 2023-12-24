from balethon import Client
from balethon.conditions import private, text

bot = Client("TOKEN")


@bot.on_message(private & text)
async def echo(message):
    await message.reply(message.text)


bot.run()
