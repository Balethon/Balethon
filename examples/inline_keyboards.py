from balethon import Client
from balethon.conditions import private
from balethon.objects import InlineKeyboard, InlineKeyboardButton

bot = Client("TOKEN")


@bot.on_message(private)
async def answer_message(client, message):
    await message.reply(
        "Click a button!",
        InlineKeyboard(
            [
                [InlineKeyboardButton("Button 1", "1")],
                [InlineKeyboardButton("Button 2", "2")]
            ]
        )
    )


@bot.on_callback_query()
async def answer_callback_query(client, callback_query):
    await callback_query.answer(
        f"Thank you for clicking on button {callback_query.data}"
    )


bot.run_polling()
