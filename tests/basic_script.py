import logging

from balethon import Client

import config

logging.basicConfig(filename="balethon.log", level=logging.INFO)

with Client(config.TOKEN) as bot:
    bot.send_message(config.USER_ID, "Test")
