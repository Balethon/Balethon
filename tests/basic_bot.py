import logging
from asyncio import sleep

from balethon import Client
from balethon.conditions import equals
from balethon.objects import Message, CallbackQuery, InlineKeyboard
from balethon.dispatcher import MonitoringChain

import config

logging.basicConfig(filename="balethon.log", level=logging.INFO)

bot = Client(config.TOKEN)
bot.include(MonitoringChain())

reply_markup = InlineKeyboard([("Button 1", "1"), ("Button 2", "2")])


@bot.on_message(equals("test"))
async def answer_message(message: Message):
    msg = await message.reply("(:")
    await sleep(2)
    await msg.edit_text("Hello from Balethon!", reply_markup)


@bot.on_callback_query()
async def answer_callback_query(callback_query: CallbackQuery):
    await callback_query.answer(f"Thanks for clicking on Button {callback_query.data} {callback_query.author.full_name}!")


if __name__ == "__main__":
    bot.run()
