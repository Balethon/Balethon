## Client.*edit_message_text()*

**ویرایش متن پیام**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که پیام در آن ویرایش می شود

- **message_id** (`str` | `int`)
    > آیدی پیامی که ویرایش می شود
    
- **text** (`str`)
    > متن جدید

- **reply_markup** (`ReplyMarkup`)
    > یک کیبورد که همراه با پیام ویرایش می شود (اختیاری)

### مقدار بازگشتی

> `Message`

### مثال

```python
await bot.edit_message_text(1234567890, 12, "Edited!")
```