---
layout: default
---

## نمونه استفاده

```python
from balethon import Client

bot = Client("TOKEN")


@bot.on_message()
async def greet(client, message):
    await message.reply("Hello")


bot.run()
```

> باید توکن را با توکنی که بات فادر در پیامرسان [بله](https://www.bale.ai/) به شما میدهد عوض کنید