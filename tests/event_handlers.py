from balethon import Client

from . import TOKEN

bot = Client(TOKEN)


@bot.on_command()
async def show_command(client, message):
    print(f"COMMAND - {message.author.full_name}: {message.text}")


@bot.on_message()
async def show_message(client, message):
    print(f"MESSAGE - {message.author.full_name}: {message.text}")


@bot.on_callback_query()
async def show_callback_query(client, callback_query):
    print(f"CALLBACK QUERY - {callback_query.author.full_name}: {callback_query.data}")


if __name__ == "__main__":
    bot.run_polling()
