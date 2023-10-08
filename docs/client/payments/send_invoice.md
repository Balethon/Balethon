## Client.*send_invoice()*

**فرستادن صورتحساب**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چتی که صورتحساب به آن فرستاده میشود

- **title** (`str`)
    > عنوان صورتحساب

- **description** (`str`)
    > توضیحات صورتحساب

- **provider_token** (`str`)
    > شماره کارت شماره کیف پول بله یا شماره درگاه و شماره پذیرنده که پول را دریافت میکند

- **prices** (`list[LabeledPrice]`)
    > لیست قیمت های برچسب دار

- **provider_data** (`str`)
    >

- **photo_url** (`str`)
    >

- **photo_size** (`int`)
    >

- **photo_width** (`int`)
    >

- **photo_height** (`int`)
    >

- **need_name** (`bool`)
    >

- **need_phone_number** (`bool`)
    >

- **need_email** (`bool`)
    >

- **need_shipping_address** (`bool`)
    >

- **is_flexible** (`bool`)
    >

- **disable_notification** (`bool`)
    >

- **reply_to_message_id** (`str` | `int`)
    >

- **reply_markup** (`ReplyMarkup`)
    >

### مقدار بازگشتی

> `Message`

### مثال

```python
await bot.send_invoice(
        chat_id=1234567890,
        title="Some title",
        description="Some description",
        provider_token="6037************",
        prices=LabeledPrice(label="Some label", amount=1000000)
    )
```