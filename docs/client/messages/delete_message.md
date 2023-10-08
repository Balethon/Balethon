## Client.*delete_message()*

**حذف پیام**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که پیام در آن حذف می شود

- **message_id** (`str` | `int`)
    > آیدی پیامی که حذف میشود
    
### مقدار بازگشتی

> `bool`

### مثال

```python
await bot.delete_message(1234567890, 12)
```