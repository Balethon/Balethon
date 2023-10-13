## Client.*send_location()*

**فرستادن پیامی حاوی موقعیت مکانی**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که پیام به آن فرستاده میشود

- **latitude** (`float`)
    > عرض جغرافیایی
    
- **longitude** (`float`)
    > طول جغرافیایی

- **reply_to_message_id** (`str` | `int`)
    > آیدی یک پیام که این پیام به آن ریپلای شود (اختیاری)

### مقدار بازگشتی

> `Message`

### مثال

```python
await bot.send_location(1234567890, 25.276987, 55.296249)
```