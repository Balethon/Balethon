from asyncio import run

from balethon import Client
from balethon.handlers import MessageHandler, CallbackQueryHandler
from config import TOKEN


async def answer_message(bot, message):
    print(f"{message.from_user['first_name']}: {message.text}")
    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "Button 1", "callback_data": "1"},
                {"text": "Button 2", "callback_data": "2"}
            ]
        ]
    }
    await message.reply("Hello from Balethon!", reply_markup)


async def answer_callback_query(bot, callback_query):
    print(f"{callback_query.from_user['first_name']}: [{callback_query.data}]")
    await callback_query.answer(f"Thank you for clicking on Button {callback_query.data}!")


async def main():
    bot = Client(TOKEN)
    bot.add_handler(MessageHandler(answer_message))
    bot.add_handler(CallbackQueryHandler(answer_callback_query))
    await bot.connect()
    await bot.polling()


if __name__ == "__main__":
    run(main())
