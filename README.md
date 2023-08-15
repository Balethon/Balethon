<p align="center">
     <a href="https://ble.ir/balethon">
         <img src="https://s8.uupload.ir/files/_balethon__ar04.png" alt="Balethon" width="400">
     </a>
     <br>
     <b>our community</b>
     <br>
     <a href="https://ble.ir/join/MGUxMTU5Yz">
         Bale
     </a>
     •
     <a href="balethon.github.io">
         Documentation
     </a>
     •
     <a href="https://t.me/balethon_GP">
         Telegram
     </a>
 </p>


<h3 align="center">A python library for creating bots in Bale</h3>

> **What is Bale?**

- > **[Bale](https://www.bale.ai/)** is a messenger with various features and the possibility of doing banking


> **How To Create Bot?**


- > you must get bot token from `@botfather` in the **Bale** and enter token in `Client()`

## Example:

```python
from balethon import Client

bot = Client("TOKEN")

@bot.on_message()
async def greet(client, message):
    await client.send_message(message["from"]["id"], "Hello")

if __name__ == "__main__":
    bot.polling()
```


> **Key Features**

- [x] **fast** TEXT
- [x] **easy** TEXT
- [x] **async** TEXT
- [x] **full documentation** TEXT

## installing:
```python
pip3 install balethon
```

## News About Balethon
- **you can find out about Balethon news and updates in [Telegram](https://t.me/balethon_py) or [Bale](https://ble.ir/balethon)**
