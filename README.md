## Balethon

Asynchronous library for creating bots in the [Bale](https://www.bale.ai/) messenger

## Usage Example

```python
from balethon import Client

bot = Client("TOKEN")


@bot.on_message()
async def greet(client, message):
    await message.reply("Hello")


bot.run_polling()
```

> You must replace "TOKEN" with the token which `@botfather` gives you in the [Bale](https://www.bale.ai/) messenger

## Installing

```bash
pip install Balethon
```

## Links

- Balethon's [documentation](https://sajjadalipour2006.github.io/Balethon/)
- Balethon's [pypi page](https://pypi.org/project/Balethon/)
- Our [news channel](https://ble.ir/balethon) in the [Bale](https://www.bale.ai/) messenger
- Our [community chat group](https://ble.ir/join/MTlhN2Q2Mz) in the [Bale](https://www.bale.ai/) messenger