from pyrogram import Client
from pyrogram import filters
from message import ReplyCheck
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["lastfm"], prefix) & filters.me)
async def lastfm(client, message):
    x = await client.get_inline_bot_results("lastfmrobot", "")
    await message.delete()
    await message.reply_inline_bot_result(x.query_id, x.results[0].id,
                                          reply_to_message_id=ReplyCheck(message),
                                          hide_via=True)
