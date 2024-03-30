<p align="center">
  <img src="https://balethon.ir/assets/img/logo.png" width="200" alt="Balethon">
</p>

## Balethon

A library for creating bots in the [Bale](https://www.bale.ai) messenger

## Quick Example

```python
from balethon import Client

bot = Client("TOKEN")


@bot.on_message()
async def greet(message):
    await message.reply("Hello")


bot.run()
```

> You must replace `TOKEN` with the token which [BotFather](https://ble.ir/botfather) gives you in the [Bale](https://www.bale.ai) messenger

## Key Features

- **[Easy](https://balethon.ir/posts/balethon-is-easy)**: Concise and high level programming interface
- **[Fast](https://balethon.ir/posts/balethon-is-fast)**: Optimized and supports asynchronous programming
- **[Documented](https://balethon.ir/posts/balethon-is-documented)**: Learn Balethon in depth with the documentation at https://balethon.ir
- **[Community](https://balethon.ir/posts/balethon-has-community)**: Active and friendly community, you are sure to get answers to your questions
- **[Design](https://balethon.ir/posts/balethon-has-design-options)**: Support for functional as well as object-oriented designs
- **[powerful](https://balethon.ir/posts/balethon-is-powerful)**: Covers the [Bale](https://www.bale.ai) messenger's api and has useful tools to make your job easier
- **[Flexible](https://balethon.ir/posts/balethon-is-flexible)**: Unable to get deprecated and ready for unexpected responses from the [Bale](https://www.bale.ai) messenger's api
- **[Intuitive](https://balethon.ir/posts/balethon-is-intuitive)**: Type-hinted and has great editor support
- **[Extensible](https://balethon.ir/posts/balethon-is-extensible)**: All balethon's systems are easily extensible

## Installing

```bash
pip install Balethon
```

## Links

- [Documentation](https://balethon.ir)
- [GitHub page](https://github.com/Balethon/Balethon)
- [Pypi page](https://pypi.org/project/Balethon)
- [Bale news channel](https://ble.ir/balethon)
- [Bale community chat group](https://ble.ir/join/MTlhN2Q2Mz)