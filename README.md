## Balethon

Asynchronous library for creating bots in the [Bale](https://www.bale.ai/) messenger

### Usage Example

```python
from balethon import Client

bot = Client("TOKEN")


@bot.on_message()
async def greet(client, message):
    await message.reply("Hello")


bot.run_polling()
```

> You must replace "TOKEN" with the token which `@botfather` gives you in the [Bale](https://www.bale.ai/) messenger

### Installing

```bash
pip install Balethon
```

### Links

- Balethon's [documentation](https://github.com/SajjadAlipour2006/Balethon/tree/main/docs/contents.md)
- Our [news channel](https://ble.ir/balethon) in the [Bale](https://www.bale.ai/) messenger
- Our [community chat group](https://ble.ir/balethon) in the [Bale](https://www.bale.ai/) messenger
- Our [news channel](https://t.me/balethon_py) in the [Telegram](https://telegram.org) messenger
- Our [community chat group](https://t.me/balethon_group) in the [Telegram](https://telegram.org) messenger