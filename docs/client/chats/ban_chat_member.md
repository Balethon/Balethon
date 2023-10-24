## Client.*ban_chat_member()*

**حذف یک عضو از یک چت**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که یک عضو از آن حذف میشود

- **user_id** (`str` | `int`)
    > آیدی عضوی که حذف میشود

### مقدار بازگشتی

> `bool`

### مثال

```python
await bot.ban_chat_member(1234567890, 123456789)
```