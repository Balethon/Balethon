## Client.*send_document()*

**فرستادن پیامی حاوی فایل**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که پیام به آن فرستاده میشود

- **document** (`str`)
    > فایلی که ارسال میشود
    
- **caption** (`str`)
    > متن پیام (اختیاری)

- **reply_to_message_id** (`str` | `int`)
    > آیدی یک پیام که این پیام به آن ریپلای شود (اختیاری)

### مقدار بازگشتی

> `Message`

### مثال

```python
await bot.send_document(1234567890, "DOCUMENT", "Hello")
```