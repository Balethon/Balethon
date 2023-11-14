## Client.*promote_chat_member()*

**تغییر دسترسی های یک عضو از یک چت**

### پارامترها

- **chat_id** (`str` | `int`)
    > آیدی چت موردنظر

- **user_id** (`str` | `int`)
    > آیدی عضو موردنظر

- **can_edit_messages** (`bool`)
    > آیا عضو موردنظر میتواند پیام های چت را ویرایش کند

- **can_delete_messages** (`bool`)
    > آیا عضو موردنظر میتواند پیام های چت را حذف کند

- **can_manage_video_chats** (`bool`)
    > آیا عضو موردنظر میتواند ویدیو چت های چت را مدیریت کند

- **can_restrict_members** (`bool`)
    > آیا عضو موردنظر میتواند اعضای چت را محدود کند

- **can_promote_members** (`bool`)
    > آیا عضو موردنظر میتواند اعضای چت را ادمین کند

- **can_change_info** (`bool`)
    > آیا عضو موردنظر میتواند اطلاعات چت را ویرایش کند

- **can_invite_users** (`bool`)
    > آیا عضو موردنظر میتواند کاربران را به چت دعوت کند

- **can_pin_messages** (`bool`)
    > آیا عضو موردنظر میتواند پیام ها را در چت سنجاق کند

- **can_send_messages** (`bool`)
    > آیا عضو موردنظر میتواند در چت پیام ارسال کند

- **can_send_media_messages** (`bool`)
    > آیا عضو موردنظر میتواند در چت پیام های دارای رسانه ارسال کند

- **can_send_media** (`bool`)
    > آیا عضو موردنظر میتواند در چت رسانه ارسال کند

- **can_send_gif_stickers** (`bool`)

- **can_reply_to_story** (`bool`)
    > آیا عضو موردنظر میتواند به وضعیت های چت ریپلای کند

- **can_forward_message_from** (`bool`)

- **can_send_gift_packet** (`bool`)

- **can_start_call** (`bool`)
    > آیا عضو موردنظر میتواند در چت تماس شروع کند

- **can_send_link_message** (`bool`)
    > آیا عضو موردنظر میتواند پیام های دارای لینک در چت ارسال کند

- **can_send_forwarded_message** (`bool`)
    > آیا عضو موردنظر میتواند در چت پیام باز ارسال کند

- **can_kick_user** (`bool`)
    > آیا عضو موردنظر میتواند اعضای چت را حذف کند

- **can_send_message** (`bool`)
    > آیا عضو موردنظر میتواند در چت پیام ارسال کند

- **can_see_members** (`bool`)
    > آیا عضو موردنظر میتواند اعضای چت را ببیند

- **can_add_story** (`bool`)
    > آیا عضو موردنظر میتواند برای چت وضعیت اضافه کند

### مقدار بازگشتی

> `bool`

### مثال

```python
await bot.promote_chat_member(1234567890, 123456789, can_promote_members=True, can_pin_messages=True)
```