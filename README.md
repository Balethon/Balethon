## Balethon

Asynchronous library for creating bots in the [Bale](https://www.bale.ai/) messanger

### Usage Example

```python
from balethon import Client

bot = Client("TOKEN")


@bot.on_message()
async def greet(client, message):
    await client.send_message(message["from"]["id"], "Hello")


if __name__ == "__main__":
    bot.run_polling()
```

> You must replace "TOKEN" with the token which `@botfather` gives you in the [Bale](https://www.bale.ai/) messanger

### Installing

```bash
pip install balethon
```

### Links

- Our [news channel](https://ble.ir/balethon) in the [Bale](https://www.bale.ai/) messanger
- Our [community chat group](https://ble.ir/balethon) in the [Bale](https://www.bale.ai/) messanger
- Our [news channel](https://t.me/balethon_py) in the [Telegram](https://telegram.org) messanger
- Our [community chat group](https://t.me/balethon_group) in the [Telegram](https://telegram.org) messanger