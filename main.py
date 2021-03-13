from pyrogram import Client
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
api_id = config.get("pyrogram", "api_id")
api_hash = config.get("pyrogram", "api_hash")
session_name = config.get("pyrogram", "session_name")
plugins = dict(root="modules")

print('______________________________________________________')
print('______________________________________________________')
print('______________________________________________________')
print('______________________________________________________')
print('UserBot Запущен! группа поддержки t.me/floodmemeframe')
print('Автор t.me/LaciaMemeFrame')
print('Статус: BETA')
print('______________________________________________________')
print('______________________________________________________')
print('______________________________________________________')
print('______________________________________________________')

Frame_UserBot = Client(session_name=session_name, api_id=api_id,
              api_hash=api_hash,
              plugins=plugins).run()