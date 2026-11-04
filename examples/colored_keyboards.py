from balethon import Client
from balethon.conditions import private
from balethon.enums import ButtonStyle
from balethon.objects import (
    InlineKeyboard,
    InlineKeyboardButton,
    ReplyKeyboard,
    ReplyKeyboardButton
)

bot = Client("TOKEN")

inline_keyboard = InlineKeyboard(
    [
        InlineKeyboardButton(
            text="Confirm",
            callback_data="confirm",
            style=ButtonStyle.SUCCESS
        ),
        InlineKeyboardButton(
            text="Cancel",
            callback_data="cancel",
            style=ButtonStyle.DANGER
        )
    ],
    [
        InlineKeyboardButton(
            text="More information",
            callback_data="info",
            style=ButtonStyle.PRIMARY
        )
    ]
)

reply_keyboard = ReplyKeyboard(
    [
        ReplyKeyboardButton(
            text="Continue",
            style=ButtonStyle.SUCCESS
        ),
        ReplyKeyboardButton(
            text="Settings",
            style=ButtonStyle.PRIMARY
        )
    ],
    [
        ReplyKeyboardButton(
            text="Cancel",
            style=ButtonStyle.DANGER
        )
    ],
    resize=True
)


@bot.on_command(private)
async def start(*, message):
    await message.reply("Choose an inline action:", inline_keyboard)
    await message.reply("Or choose a reply action:", reply_keyboard)


@bot.on_callback_query(inline_keyboard.on_click(0, 0))
async def confirm(*, callback_query):
    await callback_query.answer("Confirmed!")


@bot.on_callback_query(inline_keyboard.on_click(0, 1))
async def cancel_inline(*, callback_query):
    await callback_query.answer("Cancelled!")


@bot.on_callback_query(inline_keyboard.on_click(1, 0))
async def more_information(*, callback_query):
    await callback_query.answer("Here is more information.")


@bot.on_message(reply_keyboard.on_click(0, 0) & private)
async def continue_action(*, message):
    await message.reply("Continuing...")


@bot.on_message(reply_keyboard.on_click(0, 1) & private)
async def settings(*, message):
    await message.reply("Opening settings...")


@bot.on_message(reply_keyboard.on_click(1, 0) & private)
async def cancel_reply(*, message):
    await message.reply("Cancelled!")


bot.run()
