## Client.*send_message()*

**فرستادن پیام متنی**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که پیام به آن فرستاده میشود

- **text** (`str`)
    > متن پیام

- **reply_markup** (`ReplyMarkup`)
    > یک کیبورد که همراه با پیام به کاربر فرستاده میشود (اختیاری)

- **reply_to_message_id** (`str` | `int`)
    > آیدی یک پیام که این پیام به آن ریپلای شود (اختیاری)

### مقدار بازگشتی

> `Message`

### مثال

```python
await bot.send_message(1234567890, "Hello!")
```