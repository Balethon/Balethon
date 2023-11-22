## بلتون دو منظوره است

بلتون علاوه بر برنامه نویسی synchronous از برنامه نویسی asynchronous هم پشتیبانی میکنه\
\
یعنی این کد (روش asynchronous)

```python
@bot.on_message()
async def echo(client, message):
    await message.reply(message.text)
```

\
و این کد (روش synchronous)

```python
@bot.on_message()
def echo(client, message):
    message.reply(message.text)
```

\
هر دو قابل قبول و درست هستن\
اما بیشتر وقت ها پیشنهاد میشه که از روش asynchronous استفاده کنید\
چون میتونه باعث افزایش سرعت بات شما بشه\
برای اطلاعات بیشتر درمورد این مبحث مقاله [بلتون سریع است](./balethon_is_fast) رو مطالعه کنید