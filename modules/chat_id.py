from pyrogram import Client
from pyrogram import filters
from message import ReplyCheck
import asyncio
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["idchat"], prefix) & filters.me)
async def idchat(client, message):

    if message.chat.type in ["supergroup", "group"] and message.chat.photo:
        user = [x async for x in client.iter_chat_members(message.chat.id)]
        admin = [x async for x in client.iter_chat_members(message.chat.id, filter="administrators")]
        bot = [x async for x in client.iter_chat_members(message.chat.id, filter="bots")]
        deleted = [x async for x in client.iter_chat_members(message.chat.id) if x.user.is_deleted]
        avatar = await client.download_media(message.chat.photo.big_file_id)
        bio = await client.get_chat(f"{message.chat.id}")
        await message.reply_photo(avatar, caption=f"<b>Информация о чате {message.chat.title}\n\n"
            f"id чата: <code>{message.chat.id}</code>\n"
            f"Тип чата: <code>{message.chat.type}</code>\n"
            f"Проверенный: <code>{message.chat.is_verified}</code>\n"
            f"Скам: <code>{message.chat.is_scam}</code>\n"
            f"Создатель: <code>{message.chat.is_creator}</code>\n"
            f"DC: <code>{message.chat.dc_id}</code>\n"
            f"Ограниченный: <code>{message.chat.is_restricted}</code>\n\n"
            f"Пользователей в чате: <code>{len(user)}</code>\n"
            f"Администраторов в чате: <code>{len(admin)}</code>\n"
            f"Ботов в чате: <code>{len(bot)}</code>\n"
            f"Удаленных: <code>{len(deleted)}</code>\n\n"                                      
            f"Отправка сообщений: <code>{message.chat.permissions.can_send_messages}</code>\n"
            f"Отправка медиа: <code>{message.chat.permissions.can_send_media_messages}</code>\n"
            f"Отправка стикеров: <code>{message.chat.permissions.can_send_stickers}</code>\n"
            f"Отправка ГИФ: <code>{message.chat.permissions.can_send_animations}</code>\n"
            f"Отправка игр: <code>{message.chat.permissions.can_send_games}</code>\n"
            f"Инлайн боты: <code>{message.chat.permissions.can_use_inline_bots}</code>\n"
            f"Превью по ссылке: <code>{message.chat.permissions.can_add_web_page_previews}</code>\n"
            f"Отправка опросов: <code>{message.chat.permissions.can_send_polls}</code>\n"
            f"Информация чата: <code>{message.chat.permissions.can_change_info}</code>\n"
            f"Приглашать: <code>{message.chat.permissions.can_invite_users}</code>\n"
            f"Закреплять: <code>{message.chat.permissions.can_pin_messages}</code>\n\n"
            f"Био: <code>{bio.description}</code></b>",
            parse_mode='HTML',
            reply_to_message_id=ReplyCheck(message))
        await message.delete()
        await asyncio.sleep(0.20)

    elif message.chat.type in ["supergroup", "group"]:
        user = [x async for x in client.iter_chat_members(message.chat.id)]
        admin = [x async for x in client.iter_chat_members(message.chat.id, filter="administrators")]
        bot = [x async for x in client.iter_chat_members(message.chat.id, filter="bots")]
        deleted = [x async for x in client.iter_chat_members(message.chat.id) if x.user.is_deleted]
        bio = await client.get_chat(f"{message.chat.id}")
        await message.reply_text(f"<b>Информация о чате {message.chat.title}\n\n"
                                                  f"id чата: <code>{message.chat.id}</code>\n"
                                                  f"Тип чата: <code>{message.chat.type}</code>\n"
                                                  f"Проверенный: <code>{message.chat.is_verified}</code>\n"
                                                  f"Скам: <code>{message.chat.is_scam}</code>\n"
                                                  f"Создатель: <code>{message.chat.is_creator}</code>\n"
                                                  f"DC: <code>{message.chat.dc_id}</code>\n"
                                                  f"Ограниченный: <code>{message.chat.is_restricted}</code>\n\n"
                                                  f"Пользователей в чате: <code>{len(user)}</code>\n"
                                                  f"Администраторов в чате: <code>{len(admin)}</code>\n"
                                                  f"Ботов в чате: <code>{len(bot)}</code>\n"
                                                  f"Удаленных: <code>{len(deleted)}</code>\n\n"
                                                  f"Отправка сообщений: <code>{message.chat.permissions.can_send_messages}</code>\n"
                                                  f"Отправка медиа: <code>{message.chat.permissions.can_send_media_messages}</code>\n"
                                                  f"Отправка стикеров: <code>{message.chat.permissions.can_send_stickers}</code>\n"
                                                  f"Отправка ГИФ: <code>{message.chat.permissions.can_send_animations}</code>\n"
                                                  f"Отправка игр: <code>{message.chat.permissions.can_send_games}</code>\n"
                                                  f"Инлайн боты: <code>{message.chat.permissions.can_use_inline_bots}</code>\n"
                                                  f"Превью по ссылке: <code>{message.chat.permissions.can_add_web_page_previews}</code>\n"
                                                  f"Отправка опросов: <code>{message.chat.permissions.can_send_polls}</code>\n"
                                                  f"Информация чата: <code>{message.chat.permissions.can_change_info}</code>\n"
                                                  f"Приглашать: <code>{message.chat.permissions.can_invite_users}</code>\n"
                                                  f"Закреплять: <code>{message.chat.permissions.can_pin_messages}</code>\n\n"
                                                  f"Био: <code>{bio.description}</code></b>",
                                  parse_mode='HTML',
                                  reply_to_message_id=ReplyCheck(message))
        await message.delete()
        await asyncio.sleep(0.20)

    elif message.chat.type in ["channel"] and message.chat.photo:
        user = [x async for x in client.iter_chat_members(message.chat.id)]
        admin = [x async for x in client.iter_chat_members(message.chat.id, filter="administrators")]
        bot = [x async for x in client.iter_chat_members(message.chat.id, filter="bots")]
        avatar = await client.download_media(message.chat.photo.big_file_id)
        deleted = [x async for x in client.iter_chat_members(message.chat.id) if x.user.is_deleted]
        bio = await client.get_chat(f"{message.chat.id}")
        await message.reply_photo(avatar, caption=f"<b>Информация о чате {message.chat.title}\n\n"
            f"id чата: <code>{message.chat.id}</code>\n"
            f"Тип чата: <code>{message.chat.type}</code>\n"
            f"Проверенный: <code>{message.chat.is_verified}</code>\n"
            f"Скам: <code>{message.chat.is_scam}</code>\n"
            f"Создатель: <code>{message.chat.is_creator}</code>\n"
            f"DC: <code>{message.chat.dc_id}</code>\n"
            f"Ограниченный: <code>{message.chat.is_restricted}</code>\n\n"
            f"Пользователей в чате: <code>{len(user)}</code>\n"
            f"Администраторов в чате: <code>{len(admin)}</code>\n"
            f"Ботов в чате: <code>{len(bot)}</code>\n"
            f"Удаленных: <code>{len(deleted)}</code>\n\n"
            f"Био: <code>{bio.description}</code></b>",
            parse_mode='HTML')
        await message.delete()
        await asyncio.sleep(0.20)

    elif message.chat.type in ["channel"]:
        user = [x async for x in client.iter_chat_members(message.chat.id)]
        admin = [x async for x in client.iter_chat_members(message.chat.id, filter="administrators")]
        bot = [x async for x in client.iter_chat_members(message.chat.id, filter="bots")]
        deleted = [x async for x in client.iter_chat_members(message.chat.id) if x.user.is_deleted]
        bio = await client.get_chat(f"{message.chat.id}")
        await message.reply_text(f"<b>Информация о чате {message.chat.title}\n\n"
            f"id чата: <code>{message.chat.id}</code>\n"
            f"Тип чата: <code>{message.chat.type}</code>\n"
            f"Проверенный: <code>{message.chat.is_verified}</code>\n"
            f"Скам: <code>{message.chat.is_scam}</code>\n"
            f"Создатель: <code>{message.chat.is_creator}</code>\n"
            f"DC: <code>{message.chat.dc_id}</code>\n"
            f"Ограниченный: <code>{message.chat.is_restricted}</code>\n\n"
            f"Пользователей в чате: <code>{len(user)}</code>\n"
            f"Администраторов в чате: <code>{len(admin)}</code>\n"
            f"Ботов в чате: <code>{len(bot)}</code>\n"
            f"Удаленных: <code>{len(deleted)}</code>\n\n"
            f"Био: <code>{bio.description}</code></b>",
            parse_mode='HTML')
        await message.delete()
        await asyncio.sleep(0.20)

    elif message.chat.type in ["private", "bot"] and message.chat.photo:
        bio = await client.get_chat(f"{message.chat.id}")
        avatar = await client.download_media(message.chat.photo.big_file_id)
        await message.reply_photo(avatar, caption=f"<b>Информация о чате {message.chat.first_name}\n\n"
            f"id чата: <code>{message.chat.id}</code>\n"
            f"Тип чата: <code>{message.chat.type}</code>\n"
            f"Проверенный: <code>{message.chat.is_verified}</code>\n"
            f"Скам: <code>{message.chat.is_scam}</code>\n"
            f"Создатель: <code>{message.chat.is_creator}</code>\n"
            f"DC: <code>{message.chat.dc_id}</code>\n"
            f"Ограниченный: <code>{message.chat.is_restricted}</code>\n\n"
            f"Био: <code>{bio.bio}</code></b>",
            parse_mode='HTML')
        await message.delete()
        await asyncio.sleep(0.20)

    elif message.chat.type in ["private", "bot"]:
        bio = await client.get_chat(f"{message.chat.id}")
        await message.reply_text(f"<b>Информация о чате {message.chat.first_name}\n\n"
            f"id чата: <code>{message.chat.id}</code>\n"
            f"Тип чата: <code>{message.chat.type}</code>\n"
            f"Проверенный: <code>{message.chat.is_verified}</code>\n"
            f"Скам: <code>{message.chat.is_scam}</code>\n"
            f"Создатель: <code>{message.chat.is_creator}</code>\n"
            f"DC: <code>{message.chat.dc_id}</code>\n"
            f"Ограниченный: <code>{message.chat.is_restricted}</code>\n\n"
            f"Био: <code>{bio.bio}</code></b>",
            parse_mode='HTML')
        await message.delete()
        await asyncio.sleep(0.20)