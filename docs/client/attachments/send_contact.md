## Client.*send_contact()*

**فرستادن پیامی حاوی اطلاعات مخاطب**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که پیام به آن فرستاده میشود

- **phone_number** (`str`)
    > شماره تلفن کاربر
    
- **first_name** (`str`)
    > نام کوچک کاربر

- **last_name** (`str`)
    >  نام خانوادگی کاربر

- **reply_to_message_id** (`str` | `int`)
    > آیدی یک پیام که این پیام به آن ریپلای شود (اختیاری)

### مقدار بازگشتی

> `Message`

### مثال

```python
await bot.send_contact(1234567890, "989*********", "Ali", "Naseri")
```