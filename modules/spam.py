from pyrogram import Client
from pyrogram import filters
import asyncio
from message import ReplyCheck
import requests
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["spam"], prefix) & filters.me)
async def spam(client, message):
    await message.delete()
    times = message.command[1]
    to_spam = ' '.join(message.command[2:])
    if message.chat.type in ['supergroup', 'group', 'private', 'bot']:
        for _ in range(int(times)):
            await client.send_message(message.chat.id, to_spam, reply_to_message_id=ReplyCheck(message))
            await asyncio.sleep(0.20)


@Client.on_message(filters.command(["hentaispam"], prefix) & filters.me)
async def hentaispam(client, message):
    await message.delete()
    times = message.command[1]
    if message.chat.type in ['supergroup', 'group', 'private', 'bot']:
        for _ in range(int(times)):
            URL = f"https://nekos.life/api/v2/img/hentai"
            r = requests.get(URL, allow_redirects=True)
            r.headers
            json = r.json()
            loveurl = json['url']
            await client.send_photo(message.chat.id, loveurl, reply_to_message_id=ReplyCheck(message))
            await asyncio.sleep(0.20)
