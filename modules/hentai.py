from pyrogram import Client
from pyrogram import filters
import asyncio
import requests
from message import ReplyCheck
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["2dnudes"], prefix) & filters.me)
async def hentai(client, message):
    hentai = message.text.split(" ", maxsplit=1)[1]
    URL = f"https://nekos.life/api/v2/img/{hentai}"
    r = requests.get(URL, allow_redirects=True)
    r.headers
    json = r.json()
    loveurl = json['url']
    filetype = loveurl.split(".", maxsplit=3)[3]
    if filetype == 'gif':
        await client.send_document(message.chat.id, loveurl, reply_to_message_id=ReplyCheck(message))
    elif filetype == 'jpg':
        await client.send_photo(message.chat.id, loveurl, reply_to_message_id=ReplyCheck(message))
    else:
        await client.send_photo(message.chat.id, loveurl, reply_to_message_id=ReplyCheck(message))
    await message.delete()
    await asyncio.sleep(0.5)
