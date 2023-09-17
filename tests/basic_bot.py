from asyncio import sleep

from balethon import Client
from balethon.objects import Message, CallbackQuery

from config import TOKEN

bot = Client(TOKEN)

reply_markup = {
    "inline_keyboard": [[{"text": "Button 1", "callback_data": "1"}, {"text": "Button 2", "callback_data": "2"}]]
}


@bot.on_message()
async def answer_message(client: Client, message: Message):
    print(f"{message.author.full_name}: {message.text}")
    if message.text != "test":
        return
    msg = await message.reply("(:", reply_markup)
    await sleep(1)
    await msg.edit_text("Hello from Balethon!", reply_markup, client)


@bot.on_callback_query()
async def answer_callback_query(client, callback_query: CallbackQuery):
    print(f"{callback_query.author.full_name}: [{callback_query.data}]")
    await callback_query.answer(f"Thanks for clicking on Button {callback_query.data} {callback_query.author.full_name}!")


@bot.on_update()
def show_update(c, u):
    print(u)


if __name__ == "__main__":
    bot.run_polling()
