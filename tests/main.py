from asyncio import run

from balethon import Client

TOKEN = ""


async def callback(bot, message):
    print(message["text"])
    await bot.send_message(message["chat"]["id"], "Hello from Balethon!", reply_to_message_id=message["message_id"])


async def main():
    bot = Client(TOKEN)
    await bot.connect()
    await bot.polling(callback)


if __name__ == "__main__":
    run(main())
