from pyrogram import Client
from pyrogram import filters
import TenGiphPy
from message import ReplyCheck
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["tenor"], prefix) & filters.me)
async def tenor(client, message):
    try:
        text = message.text.split(" ", maxsplit=1)[1]
    except:
        await message.edit("<b>Че искать?</b>")
    tenor = TenGiphPy.Tenor(token='QP1YSSQ1SMLE')
    await client.send_document(message.chat.id,
                               tenor.random(f"{text}"),
                               reply_to_message_id=ReplyCheck(message))
    await message.delete()


@Client.on_message(filters.command(["giphy"], prefix) & filters.me)
async def giphy(client, message):
    try:
        text = message.text.split(" ", maxsplit=1)[1]
    except:
        await message.edit("<b>Че искать?</b>")
    giphy = TenGiphPy.Giphy(token='6ZUBM93529TyHu3EIGEmNNybmKfjZ1DZ')
    await client.send_document(message.chat.id,
                               giphy.random(tag=f"{text}")['data']['images']['downsized_large']['url'],
                               reply_to_message_id=ReplyCheck(message))
    await message.delete()
