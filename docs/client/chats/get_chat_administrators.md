## Client.*get_chat_administrators()*

**دریافت ادمین های یک چت**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که ادمین های آن دریافت میشود

### مقدار بازگشتی

> `list`[`ChatMember`]

### مثال

```python
await bot.get_chat_administrators(1234567890)
```