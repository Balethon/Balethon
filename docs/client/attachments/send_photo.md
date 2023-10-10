## Client.*send_photo()*

**فرستادن پیام دارای عکس**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که پیام به آن فرستاده میشود

- **photo** (`str`)
    > عکسی که فرستاده می شود

- **caption** (`str`)
    > متن پیام (اختیاری)

- **reply_to_message_id** (`str` | `int`)
    > آیدی یک پیام که این پیام به آن ریپلای شود (اختیاری)

### مقدار بازگشتی

> `Message`

### مثال

```python
await bot.send_photo(1234567890, "PHOTO", "Hello")
```