from pyrogram import Client
from pyrogram import filters
import time
import os
import asyncio
import configparser
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")
download_directory = config.get("pyrogram", "download_directory")


@Client.on_message(filters.command(["filesd"], prefix) & filters.me)
async def filesd(client, message):
    user_msg = message.text.split(" ", maxsplit=1)[1]
    if not message.reply_to_message:
        await message.edit("<b>Нет ответа.</b>", parse_mode='HTML')
    start = int(time.time())
    await client.download_media(message.reply_to_message, file_name=f"{download_directory}/{user_msg}")
    res = int(time.time()) - start
    await asyncio.sleep(0.5)
    await message.edit(
        f"<b>Файл сохранен\nСсылка на файл: {download_directory}/{user_msg}\nСкачано за {res} секунд(ы)</b>",
        parse_mode='HTML')
    await asyncio.sleep(0.5)
    print({client.download_media})


@Client.on_message(filters.command(["filesu"], prefix) & filters.me)
async def filesu(client, message):
    user_msg = message.text.split(" ", maxsplit=1)[1]
    start = int(time.time())
    await client.send_document(message.chat.id, f'{download_directory}/{user_msg}')
    res = int(time.time()) - start
    await asyncio.sleep(0.5)
    print({client.send_document})
    await message.edit(f"<b>Файл загружен за {res} секунд(ы)</b>", parse_mode='HTMl')
