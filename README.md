## Balethon

Asynchronous library for creating bots in the [Bale](https://www.bale.ai/) messenger

### Usage Example

```python
from balethon import Client

bot = Client("TOKEN")


@bot.on_message()
async def greet(client, message):
    await message.reply("Hello")


bot.run_polling()
```

> You must replace "TOKEN" with the token which `@botfather` gives you in the [Bale](https://www.bale.ai/) messenger

### Installing

```bash
pip install Balethon
```

### Documentation

* [client](https://github.com/SajjadAlipour2006/Balethon/tree/main/docs/client)

  * [attachments](https://github.com/SajjadAlipour2006/Balethon/tree/main/docs/client/attachments)
     * [get_file](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/attachments/get_file.md#clientget_file)
     * [send_audio](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/attachments/send_audio.md#clientsend_audio)
     * [send_contact](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/attachments/send_contact.md#clientsend_contact)
     * [send_document](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/attachments/send_document.md#clientsend_document)
     * [send_location](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/attachments/send_location.md#clientsend_location)
     * [send_photo](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/attachments/send_photo.md#clientsend_photo)
     * [send_video](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/attachments/send_video.md#clientsend_video)
     * [send_voice](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/attachments/send_voice.md#clientsend_voice)

  * [chats](https://github.com/SajjadAlipour2006/Balethon/tree/main/docs/client/chats)
     *  [get_chat](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/chats/get_chat.md#clientget_chat)
     *  [get_chat_administrators](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/chats/get_chat_administrators.md#clientget_chat_administrators)
     *  [get_chat_member](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/chats/get_chat_member.md#clientget_chat_member)
     *  [get_chat_members_count](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/chats/get_chat_members_count.md#clientget_chat_members_count)

  * [messages](https://github.com/SajjadAlipour2006/Balethon/tree/main/docs/client/messages)
     *  [delete_message](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/messages/delete_message.md#clientdelete_message)
     *  [edit_message_text](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/messages/edit_message_text.md#clientedit_message_text)
     *  [send_message](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/messages/send_message.md#clientsend_message)

  * [payments](https://github.com/SajjadAlipour2006/Balethon/tree/main/docs/client/payments)
     * [send_invoice](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/payments/send_invoice.md#clientsend_invoice)

  * [updates](https://github.com/SajjadAlipour2006/Balethon/tree/main/docs/client/updates)
     * [delete_webhook](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/updates/delete_webhook.md#clientdelete_webhook)
     * [get_updates](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/updates/get_updates.md#clientget_updates)
     * [set_webhook](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/updates/set_webhook.md#clientset_webhook)

  * [users](https://github.com/SajjadAlipour2006/Balethon/tree/main/docs/client/users)
     * [get_me](https://github.com/SajjadAlipour2006/Balethon/blob/main/docs/client/users/get_me.md#clientget_me)

### Links

- Our [news channel](https://ble.ir/balethon) in the [Bale](https://www.bale.ai/) messenger
- Our [community chat group](https://ble.ir/balethon) in the [Bale](https://www.bale.ai/) messenger
- Our [news channel](https://t.me/balethon_py) in the [Telegram](https://telegram.org) messenger
- Our [community chat group](https://t.me/balethon_group) in the [Telegram](https://telegram.org) messenger