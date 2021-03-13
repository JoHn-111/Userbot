from pyrogram import Client
from pyrogram import filters
import asyncio
from message import ReplyCheck
import configparser
import os
import sys

config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["whois"], prefix) & filters.me)
async def whois(client, message):
    if message.reply_to_message.from_user.photo:
        user = message.reply_to_message.from_user
        last_name = f"{user.last_name}" if user.last_name is not None else "Нету"
        username = f"@{user.username}" if user.username is not None else "Нету"
        bio = await client.get_chat(f"{user.id}")
        common_chats = len(await client.get_common_chats(user.id))
        avatar_count = await client.get_profile_photos_count(f"{user.id}")
        avatar = await client.download_media(user.photo.big_file_id)
        await message.reply_photo(avatar, caption=f"<b>ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ:\n\n"
                                                  f"Имя: <code>{user.first_name}</code>\n"
                                                  f"Фамилия: <code>{last_name}</code>\n"
                                                  f"Юзернейм: <code>{username}</code>\n"
                                                  f"Контакт: <code>{user.is_contact}</code>\n"
                                                  f"Взаимный контакт: <code>{user.is_mutual_contact}</code>\n"
                                                  f"Удален: <code>{user.is_deleted}</code>\n"
                                                  f"Скам: <code>{user.is_scam}</code>\n"
                                                  f"Поддержка: <code>{user.is_support}</code>\n"
                                                  f"Статус: <code>{user.status}</code>\n"
                                                  f"ID: <code>{user.id}</code>\n"
                                                  f"Бот: <code>{user.is_bot}</code>\n"
                                                  f"Ограничен: <code>{user.is_restricted}</code>\n"
                                                  f"Верифицирован: <code>{user.is_verified}</code>\n\n"
                                                  f"Био:\n<code>{bio.bio}</code>\n\n"
                                                  f"Кол-во аватарок в профиле: <code>{avatar_count}</code>\n"
                                                  f"Общие чаты: <code>{common_chats}</code>\n"
                                                  f"Пермалинк: {message.reply_to_message.from_user.mention}\n"
                                                  f"DC: <code>{user.dc_id}</code></b>",
                                  parse_mode='HTML',
                                  reply_to_message_id=ReplyCheck(message))
        await message.delete()
        await asyncio.sleep(0.20)

    elif message.reply_to_message.from_user.is_deleted:
        user = message.reply_to_message.from_user
        last_name = f"{user.last_name}" if user.last_name is not None else "Нету"
        username = f"@{user.username}" if user.username is not None else "Нету"
        bio = await client.get_chat(f"{user.id}")
        common_chats = len(await client.get_common_chats(user.id))
        avatar_count = await client.get_profile_photos_count(f"{user.id}")
        await message.reply_text(text=f"<b>ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ:\n\n"f"Имя: <code>{user.first_name}</code>\n"
                                      f"Фамилия: <code>{last_name}</code>\n"
                                      f"Юзернейм: <code>{username}</code>\n"
                                      f"Контакт: <code>{user.is_contact}</code>\n"
                                      f"Взаимный контакт: <code>{user.is_mutual_contact}</code>\n"
                                      f"Удален: <code>{user.is_deleted}</code>\n"
                                      f"Скам: <code>{user.is_scam}</code>\n"
                                      f"Поддержка: <code>{user.is_support}</code>\n"
                                      f"Статус: <code>{user.status}</code>\n"
                                      f"ID: <code>{user.id}</code>\n"
                                      f"Бот: <code>{user.is_bot}</code>\n"
                                      f"Ограничен: <code>{user.is_restricted}</code>\n"
                                      f"Верифицирован: <code>{user.is_verified}</code>\n\n"
                                      f"Био:\n<code>{bio.bio}</code>\n\n"
                                      f"Кол-во аватарок в профиле: <code>{avatar_count}</code>\n"
                                      f"Общие чаты: <code>{common_chats}</code>\n"
                                      f"DC: <code>{user.dc_id}</code></b>",
                                 parse_mode='HTML',
                                 reply_to_message_id=ReplyCheck(message))
        await message.delete()
        await asyncio.sleep(0.20)

    else:
        user = message.reply_to_message.from_user
        last_name = f"{user.last_name}" if user.last_name is not None else "Нету"
        username = f"@{user.username}" if user.username is not None else "Нету"
        bio = await client.get_chat(f"{user.id}")
        common_chats = len(await client.get_common_chats(user.id))
        avatar_count = await client.get_profile_photos_count(f"{user.id}")
        await message.reply_text(text=f"<b>ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ:\n\n"f"Имя: <code>{user.first_name}</code>\n"
                                      f"Фамилия: <code>{last_name}</code>\n"
                                      f"Юзернейм: <code>{username}</code>\n"
                                      f"Контакт: <code>{user.is_contact}</code>\n"
                                      f"Взаимный контакт: <code>{user.is_mutual_contact}</code>\n"
                                      f"Удален: <code>{user.is_deleted}</code>\n"
                                      f"Скам: <code>{user.is_scam}</code>\n"
                                      f"Поддержка: <code>{user.is_support}</code>\n"
                                      f"Статус: <code>{user.status}</code>\n"
                                      f"ID: <code>{user.id}</code>\n"
                                      f"Бот: <code>{user.is_bot}</code>\n"
                                      f"Ограничен: <code>{user.is_restricted}</code>\n"
                                      f"Верифицирован: <code>{user.is_verified}</code>\n\n"
                                      f"Био:\n<code>{bio.bio}</code>\n\n"
                                      f"Кол-во аватарок в профиле: <code>{avatar_count}</code>\n"
                                      f"Общие чаты: <code>{common_chats}</code>\n"
                                      f"Пермалинк: {message.reply_to_message.from_user.mention}\n"
                                      f"DC: <code>{user.dc_id}</code></b>",
                                 parse_mode='HTML',
                                 reply_to_message_id=ReplyCheck(message))
        await message.delete()
        await asyncio.sleep(0.20)
