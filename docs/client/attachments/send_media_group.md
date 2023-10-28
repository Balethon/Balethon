## Client.*send_media_group()*

**فرستادن پیام دارای یک گروه از رسانه های مختلف**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که پیام به آن فرستاده میشود

- **media** (`list`[`InputMedia` | `InputMediaPhoto` | `InputMediaVideo`])
    > رسانه هایی که فرستاده می شوند، باید یک لیست باشد که آبجکت های اینپوت مدیا میتوانند در آن فرار بگیرند

### مقدار بازگشتی

> `Message`

### مثال

```python
await bot.send_media_group(1234567890, [InputMediaPhoto("photo.jpg"), InputMediaVideo("video.mp4")])
```