## پرداخت ها

**به این بات یک پیام بدهید تا یک پیام دارای صورتحساب به شما بفرستد\
سپس میتوانید مبلغی را توسط آن پرداخت کنید**

```python
from balethon import Client
from balethon.conditions import private
from balethon.objects import LabeledPrice

bot = Client("TOKEN")

PROVIDER_TOKEN = "6037************"


@bot.on_message(private)
async def send_invoice(client, message):
    await client.send_invoice(
        chat_id=message.chat.id,
        title="Some title",
        description="Some description",
        provider_token=PROVIDER_TOKEN,
        prices=LabeledPrice(label="Some label", amount=1000000)
    )


@bot.on_pre_checkout_query()
async def show_pre_checkout_query(client, pre_checkout_query):
    user = pre_checkout_query.author.full_name
    payload = pre_checkout_query.invoice_payload
    print(f"{user} paid {payload}")


bot.run()
```