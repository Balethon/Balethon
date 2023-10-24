## Client.*forward_message()*

**باز ارسال کردن پیام**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که پیام در آن باز ارسال خواهد شد

- **from_chat_id** (`str` | `int`)
    > آیدی چتی که پیام در آن قرار دارد

- **message_id** (`str` | `int`)
    > آیدی پیامی که باز ارسال میشود

### مقدار بازگشتی

> `Message`

### مثال

```python
await bot.forward_message(1234567890, 1234567890, 12)
```