from balethon import Client
from balethon.conditions import private, successful_payment
from balethon.objects import LabeledPrice

bot = Client("TOKEN")

PROVIDER_TOKEN = "6037************"


@bot.on_message(successful_payment)
async def show_payment(client, message):
    user = await client.get_chat(message.successful_payment.invoice_payload)
    amount = message.successful_payment.total_amount
    print(f"{user.full_name} paid {amount}")


@bot.on_message(private)
async def send_invoice(client, message):
    await client.send_invoice(
        chat_id=message.chat.id,
        title="Some title",
        description="Some description",
        payload=str(message.author.id),
        provider_token=PROVIDER_TOKEN,
        prices=[LabeledPrice(label="Some label", amount=1000000)]
    )


bot.run()
