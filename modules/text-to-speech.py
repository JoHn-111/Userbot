from pyrogram import Client
from pyrogram import filters
from gtts import gTTS
from io import BytesIO
from message import ReplyCheck
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["tts"], prefix) & filters.me)
async def tts(client, message):
    lang = message.command[1]
    text = ' '.join(message.command[2:])
    await message.edit('<code>Обработка...</code>')
    tts = gTTS(text, lang=lang)
    voice = BytesIO()
    tts.write_to_fp(voice)
    voice.name = 'voice.ogg'
    await message.delete()
    await client.send_audio(message.chat.id, voice, reply_to_message_id=ReplyCheck(message))
