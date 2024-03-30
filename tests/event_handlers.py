from balethon import Client

from config import TOKEN

bot = Client(TOKEN)


@bot.on_connect()
async def connection():
    print("CONNECTED")


@bot.on_initialize()
async def initialization():
    print("INITIALIZED")


@bot.on_command()
async def show_command(message):
    print(f"COMMAND - {message.author.full_name}: {message.text}")


@bot.on_message()
async def show_message(message):
    print(f"MESSAGE - {message.author.full_name}: {message.text}")


@bot.on_edited_message()
async def show_edited_message(edited_message):

    print(f"EDITED MESSAGE - {edited_message.author.full_name}: {edited_message.text}")


@bot.on_callback_query()
async def show_callback_query(callback_query):
    print(f"CALLBACK QUERY - {callback_query.author.full_name}: {callback_query.data}")


@bot.on_pre_checkout_query()
async def show_pre_checkout_query(pre_checkout_query):
    print(f"PRE CHECKOUT QUERY - {pre_checkout_query.author.full_name}: {pre_checkout_query}")


@bot.on_shipping_query()
async def show_shipping_query(shipping_query):
    print(f"SHIPPING QUERY {shipping_query.author.full_name}: {shipping_query}")


@bot.on_error()
async def show_error(error):
    print(f"ERROR - {error}")


@bot.on_shutdown()
async def shutting_down():
    print("SHUTTING DOWN")


@bot.on_disconnect()
async def disconnection():
    print("DISCONNECTED")


@bot.on_update()
async def show_update(update):
    print(f"UPDATE - {update.author.full_name}: {update}")


@bot.on_event()
async def show_event(event):
    print(f"EVENT - {event}")


if __name__ == "__main__":
    bot.run()
