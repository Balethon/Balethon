## class balethon.objects.*Message*

**این کلاس به عنوان یک پیام ایفای نقش میکند**

### پارامترها

- **id** (`int`)
    > آیدی پیام

- **author** (`User`)
    >  فرستنده پیام

- **date** (`Date`)
    >  تاریخ فرستاده شدن پیام

- **chat** (`Chat`)
    >  چتی که این پیام در آن فرستاده شد

- **forward_from** (`User`)
    >  کاربری که پیامش فوروارد شده

- **forward_from_chat** (`Chat`)
    >  چتی که پیام از آن فوروارد شده

- **forward_from_message_id** (`int`)
    >  آیدی پیام اصلی که این پیام فوروارد شده از آن است

- **forward_date** (`Date`)
    >  تاریخ فوروارد

- **reply_to_message** (`Message`)
    >  پیامی که این پیام به آن ریپلای شده

- **edit_date** (`Date`)
    >  تاریخ ویرایش

- **text** (`str`)
    >  متن پیام

- **entities**
    >  

- **caption_entities**
    >  

- **audio**
    >  

- **document**
    >  

- **photo**
    >  

- **video**
    >  

- **voice**
    >  

- **caption**
    >  

- **contact**
    >  

- **location**
    >  

- **new_chat_members**
    >  

- **left_chat_member**
    >  

- **new_chat_title**
    >  

- **new_chat_photo**
    > 

- **delete_chat_photo**
    > 

- **group_chat_created**
    > 

- **supergroup_chat_created**
    > 

- **channel_chat_created**
    > 

- **pinned_message**
    > 

- **invoice**
    > 

- **successful_payment**
    >