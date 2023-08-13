from balethon import Client
from config import TOKEN

bot = Client(TOKEN)


@bot.on_message()
async def answer_message(client, message):
    print(f"{message['from']['first_name']}: {message['text']}")
    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "Button 1", "callback_data": "1"},
                {"text": "Button 2", "callback_data": "2"}
            ]
        ]
    }
    await client.send_message(message["chat"]["id"], "Hello from Balethon!", reply_markup, message["message_id"])


@bot.on_callback_query()
async def answer_callback_query(client, callback_query):
    print(f"{callback_query['from']['first_name']}: [{callback_query['data']}]")
    await client.send_message(callback_query["from"]["id"], f"Thank you for clicking on Button {callback_query['data']}!")


if __name__ == "__main__":
    bot.polling()
