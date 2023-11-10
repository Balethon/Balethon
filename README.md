<p align="center">
  <img src="logo.png" width="200" alt="Balethon">
</p>

## Balethon

Asynchronous library for creating bots in the [Bale](https://www.bale.ai) messenger

## Usage Example

```python
from balethon import Client

bot = Client("TOKEN")


@bot.on_message()
async def greet(client, message):
    await message.reply("Hello")


bot.run_polling()
```

> You must replace "TOKEN" with the token which [@botfather](https://ble.ir/botfather) gives you in the [Bale](https://www.bale.ai) messenger

## Key Features

- **Easy**: Does the heavy job and requires minimal work from the user
- **Fast**: Optimized and asynchronous
- **Documented**: Learn Balethon in depth with the documentation at https://sajjadalipour2006.github.io/Balethon
- **Community**: Active and friendly community at https://ble.ir/join/MTlhN2Q2Mz, you are sure to find answers to your questions
- **Design**: Support for functional and object-oriented designs
- **powerful**: Covers the bale messenger's api and has powerful tools to make your job easier
- **Flexible**: Unable to deprecate and ready for unexpected responses from the Bale messenger's api
- **Intuitive**: Type-hinted and has great editor support

## Installing

```bash
pip install Balethon
```

## Links

- Our [documentation](https://sajjadalipour2006.github.io/Balethon)
- Our [gitHub page](https://github.com/SajjadAlipour2006/Balethon)
- Our [pypi page](https://pypi.org/project/Balethon)
- Our [news channel](https://ble.ir/balethon) in the [Bale](https://www.bale.ai) messenger
- Our [community chat group](https://ble.ir/join/MTlhN2Q2Mz) in the [Bale](https://www.bale.ai) messenger