import logging
from asyncio import sleep

from balethon import Client
from balethon.objects import Message, CallbackQuery, InlineKeyboard

import config

logging.basicConfig(filename="balethon.log", level=logging.INFO)

bot = Client(config.TOKEN)

reply_markup = InlineKeyboard([("Button 1", "1"), ("Button 2", "2")])


@bot.on_connect()
def connected(client, time):
    print(f"{client} is connected! {time}")


@bot.on_message()
async def answer_message(message: Message):
    print(f"{message.author.full_name}: {message.text}")
    if message.text != "test":
        return
    msg = await message.reply("(:")
    await sleep(1)
    await msg.edit_text("Hello from Balethon!", reply_markup)


@bot.on_callback_query()
async def answer_callback_query(callback_query: CallbackQuery):
    print(f"{callback_query.author.full_name}: [{callback_query.data}]")
    await callback_query.answer(
        f"Thanks for clicking on Button {callback_query.data} {callback_query.author.full_name}!"
    )


@bot.on_disconnect()
def disconnected(client, time):
    print(f"{client} is disconnected! {time}")


if __name__ == "__main__":
    bot.run()
