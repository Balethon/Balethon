## Client.*get_chat_members_count()*

**دریافت تعداد اعضای یک چت**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که تعداد اعضای آن دریافت میشود

### مقدار بازگشتی

> `int`

### مثال

```python
await bot.get_chat_members_count(1234567890)
```