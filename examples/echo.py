from balethon import Client
from balethon.conditions import text

bot = Client("TOKEN")


@bot.on_message(text)
async def echo(client, message):
    await client.send_message(message["from"]["id"], message["text"], reply_to_message_id=message["message_id"])


if __name__ == "__main__":
    bot.polling()
