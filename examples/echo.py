from balethon import Client
from balethon.conditions import private, text

bot = Client("TOKEN")


@bot.on_message(private & text)
async def echo(client, message):
    await message.reply(message.text)


if __name__ == "__main__":
    bot.run_polling()
