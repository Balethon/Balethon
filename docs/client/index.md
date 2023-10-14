## class balethon.*Client*

**این کلاس به عنوان یک بات بله ایفای نقش میکند و ابزار اصلی ارتباط با بله است**

### پارامترها

- **token** (`str`)
    > توکن بات که از بات فادر گرفته میشود

- **time_out** (`int`)
    >  مهلت ارسال درخواست ها تا قبل از لغو شدن و پرتاب ارور (اختیاری)

* [attachments](./attachments/)
   * [get_file](./attachments/get_file)
   * [send_audio](./attachments/send_audio)
   * [send_contact](./attachments/send_contact)
   * [send_document](./attachments/send_document)
   * [send_location](./attachments/send_location)
   * [send_photo](./attachments/send_photo)
   * [send_video](./attachments/send_video)
   * [send_voice](./attachments/send_voice)

* [chats](./chats/)
   *  [get_chat](./chats/get_chat)
   *  [get_chat_administrators](./chats/get_chat_administrators)
   *  [get_chat_member](./chats/get_chat_member)
   *  [get_chat_members_count](./chats/get_chat_members_count)

* [messages](./messages/)
   *  [delete_message](./messages/delete_message)
   *  [edit_message_text](./messages/edit_message_text)
   *  [send_message](./messages/send_message)

* [payments](./payments/)
   * [send_invoice](./payments/send_invoice)

* [updates](./updates/)
   * [delete_webhook](./updates/delete_webhook)
   * [get_updates](./updates/get_updates)
   * [set_webhook](./updates/set_webhook)

* [users](./users/)
   * [get_me](./users/get_me)