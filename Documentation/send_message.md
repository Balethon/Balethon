 **Client.send_message**

- chat_id <kbd>str | int</kbd>
    > **چت آیدی مورد نظر که میخواهید پیام به اون چت ارسال بشه**

- text <kbd>str</kbd>
    > **پیامی که میخواید به چت مورد نظر ارسال بشه**

- reply_markup <kbd>optional(InlineKeyboard | ReplyKeyboard)</kbd>
    > **حالا صبر کن**

- reply_to_message_id <kbd>str | int</kbd>
    > **اگر میخواهید پیام شما به پیامی ریپلای شود، مسیج آیدی آن پیام را در این قسمت قرار دهید**


```python
await bot.send_message(123456, "Hello balethon !")

```