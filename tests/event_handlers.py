from balethon import Client

from config import TOKEN

bot = Client(TOKEN)


@bot.on_event()
async def show_event(client, event):
    print(f"EVENT - {event}")


@bot.on_connect()
async def connection(client):
    print("CONNECTED")


@bot.on_update()
async def show_update(client, update):
    print(f"UPDATE - {update.author.full_name}: {update}")


@bot.on_command()
async def show_command(client, message):
    print(f"COMMAND - {message.author.full_name}: {message.text}")


@bot.on_message()
async def show_message(client, message):
    print(f"MESSAGE - {message.author.full_name}: {message.text}")


@bot.on_callback_query()
async def show_callback_query(client, callback_query):
    print(f"CALLBACK QUERY - {callback_query.author.full_name}: {callback_query.data}")


@bot.on_pre_checkout_query()
async def show_pre_checkout_query(client, pre_checkout_query):
    print(f"PRE CHECKOUT QUERY - {pre_checkout_query.author.full_name}: {pre_checkout_query}")


@bot.on_shipping_query()
async def show_shipping_query(client, shipping_query):
    print(f"SHIPPING QUERY {shipping_query.author.full_name}: {shipping_query}")


@bot.on_error()
async def show_error(client, error):
    print(f"ERROR - {error}")


@bot.on_disconnect()
async def disconnection(client):
    print("DISCONNECTED")


if __name__ == "__main__":
    bot.run_polling()
