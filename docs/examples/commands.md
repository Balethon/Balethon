## کامندها

**این بات 4 دستور دارد\
/start\
/help\
/say_hello\
/count_to_ten\
آن ها را تست کنید**

```python
from balethon import Client
from balethon.conditions import private

bot = Client("TOKEN")


@bot.on_command(private)
async def start(client, message):
    await message.reply(
        "Hello, I'm the commands bot\nUse /help to see my commands"
    )


@bot.on_command(private, name="help")
async def help_command(client, message):
    await message.reply("/say_hello\n/count_to_ten")


@bot.on_command(private)
async def say_hello(client, message):
    await message.reply("Hello my dear and precious user!")


@bot.on_command(private)
async def count_to_ten(client, message):
    counting_message = await message.reply(
        "I will start to count to ten now"
    )
    for i in range(1, 11):
        await counting_message.edit_text(str(i))


bot.run_polling()
```