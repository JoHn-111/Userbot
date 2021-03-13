from pyrogram import Client
from pyrogram import filters
import asyncio
import random
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["quote"], prefix) & filters.me)
async def quote(client, message):
    if not message.reply_to_message:
        await message.edit("<b>Нету ответа на сообщение</b>", parse_mode='HTML')
        return
    await message.edit("<b>Создание...</b>", parse_mode='HTML')
    await message.reply_to_message.forward("@QuotLyBot")
    is_sticker = False
    progress = 0
    while not is_sticker:
        try:
            msg = await Client.get_history("@QuotLyBot", 1)
            check = msg[0]["sticker"]["file_id"]
            is_sticker = True
        except:
            await asyncio.sleep(0.5)
            progress += random.randint(0, 10)
            try:
                await message.edit("<b>Создание...</b>\n<b>Обработка... {}%</b>".format(progress), parse_mode='HTML')
            except:
                await message.edit("<b>Ошибка.</b>", parse_mode='HTML')
    await message.edit("<b>Создано</b>", parse_mode='HTML')
    msg_id = msg[0]["message_id"]
    await message.delete()
    await Client.forward_messages(message.chat.id, "@QuotLyBot", msg_id)
