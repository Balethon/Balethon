from asyncio import get_event_loop

from balethon import Client
from balethon.handlers import MessageHandler, CallbackQueryHandler
from config import TOKEN


async def answer_message(bot, message):
    print(message)
    print(f"{message.from_user.id}: {message.text}")
    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "Button 1", "callback_data": "1"},
                {"text": "Button 2", "callback_data": "2"}
            ]
        ]
    }
    await bot.send_message(message.chat.id, "Hello from Balethon!", reply_markup, message.id)


async def answer_callback_query(bot, callback_query):
    print(f"{callback_query['from']['first_name']}: [{callback_query['data']}]")
    await bot.send_message(callback_query['from']["id"], f"Thank you for clicking on Button {callback_query['data']}!")


async def main():
    bot = Client(TOKEN)
    bot.add_handler(MessageHandler(answer_message))
    bot.add_handler(CallbackQueryHandler(answer_callback_query))
    await bot.connect()
    await bot.polling()


if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(main())
