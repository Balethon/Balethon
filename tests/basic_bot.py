from asyncio import sleep

from balethon import Client
from balethon.objects import Message, CallbackQuery

from config import TOKEN

bot = Client(TOKEN)

reply_markup = {
    "inline_keyboard": [
        [
            {"text": "Button 1", "callback_data": "1"},
            {"text": "Button 2", "callback_data": "2"}
        ]
    ]
}


@bot.on_message()
async def answer_message(client, message: Message):
    print(f"{message.author.full_name}: {message.text}")
    if message.text != "test":
        return
    msg = await message.reply("(:", reply_markup)
    await sleep(1)
    await client.edit_message_text(msg["chat"]["id"], msg["message_id"], "Hello from Balethon!", reply_markup)
    await sleep(1)


@bot.on_callback_query()
async def answer_callback_query(client, callback_query: CallbackQuery):
    print(f"{callback_query.author.full_name}: [{callback_query.data}]")
    await client.send_message(callback_query.message.chat.id, f"Thanks for clicking on Button {callback_query.data} {callback_query.author.full_name}!")


if __name__ == "__main__":
    bot.run_polling()
