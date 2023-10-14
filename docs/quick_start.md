---
layout: default
---

## مثال استفاده

```python
from balethon import Client

bot = Client("TOKEN")


@bot.on_message()
async def greet(client, message):
    await message.reply("Hello")


bot.run_polling()
```

> باید توکن را با توکنی که بات فادر در پیامرسان [بله](https://www.bale.ai/) به شما میدهد عوض کنید

## نصب کردن

```bash
pip install Balethon
```

[قبلی](./)
[بعدی](./client/index)