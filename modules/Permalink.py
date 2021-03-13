from pyrogram import Client
from pyrogram import filters
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["permalink"], prefix) & filters.me)
async def permalink(client, message):
    text = message.text.split(" ", maxsplit=2)[2]
    user_idsuser = message.text.split(" ", maxsplit=2)[1]
    await message.edit(f"<b>{text} <a href='tg://user?id={user_idsuser}'>permalink</a></b>")
