## بات اکو

**اگر به پیوی این بات یک پیام ارسال کنید با یک پیام با همان متن به شما پاسخ میدهد**

```python
from balethon import Client
from balethon.conditions import private, text

bot = Client("TOKEN")


@bot.on_message(private & text)
async def echo(client, message):
    await message.reply(message.text)


bot.run()
```