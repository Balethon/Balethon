from balethon import Client
from balethon.conditions import private
from balethon.objects import InlineKeyboard

bot = Client("TOKEN")


@bot.on_message(private)
async def answer_message(client, message):
    await message.reply(
        "Click a button!",
        InlineKeyboard(
            [("Button 1", "1")],
            [("Button 2", "2")]
        )
    )


@bot.on_callback_query()
async def answer_callback_query(client, callback_query):
    await callback_query.answer(
        f"Thank you for clicking on button {callback_query.data}"
    )


bot.run()
