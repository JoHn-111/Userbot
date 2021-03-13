import html
import random
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import ChatPermissions
from pyrogram.errors import ChatAdminRequired, UsernameInvalid, PeerIdInvalid, UserIdInvalid, FloodWait
from message import admin_check, is_sudoadmin, ReplyCheck, mention_html
import asyncio
import time
from emoji import get_emoji_regexp
import configparser
import os
import sys

config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_stickers=False,
    can_send_animations=False,
    can_send_games=False,
    can_use_inline_bots=False,
    can_add_web_page_previews=False,
    can_send_polls=False,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False
)

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_stickers=True,
    can_send_animations=True,
    can_send_games=True,
    can_use_inline_bots=True,
    can_add_web_page_previews=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False
)


@Client.on_message(filters.command(["pin"], prefix) & filters.me)
async def pin(client, message):
    if message.chat.type in ['group', 'supergroup']:
        chat_id = message.chat.id
        get_group = await client.get_chat(chat_id)
        can_pin = await admin_check(message)
        if can_pin:
            try:
                if message.reply_to_message:
                    disable_notification = True
                    if len(message.command) >= 2 and message.command[1] in ['alert', 'notify', 'loud']:
                        disable_notification = False
                    await client.pin_chat_message(
                        message.chat.id,
                        message.reply_to_message.message_id,
                        disable_notification=disable_notification
                    )
                    await message.edit(
                        f"<b>Сообщение закреплено</b>\n"
                        f"<b>Чат: {get_group.title} ({chat_id})</b>",
                        parse_mode='HTML')
                else:
                    await message.edit("<b>Закреплять нечего</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
            except Exception as e:
                await message.edit(
                    f"<b>{e}</b>",
                    parse_mode='HTML')
                return
        else:
            await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
    else:
        await message.delete()


@Client.on_message(filters.command(["del"], prefix) & filters.me)
async def deli(client, message):
    try:
        await message.reply_to_message.delete()
    except:
        pass

    try:
        await message.delete()
    except:
        pass


@Client.on_message(filters.command(["mute"], prefix) & filters.me)
async def mute(client, message):
    if message.chat.type in ['group', 'supergroup']:
        chat_id = message.chat.id
        get_group = await client.get_chat(chat_id)
        can_mute = await admin_check(message)
        if can_mute:
            if message.reply_to_message:
                try:
                    get_mem = await client.get_chat_member(
                        chat_id,
                        message.reply_to_message.from_user.id
                    )
                    if len(message.text.split()) == 2 and message.text.split()[1] == "24":
                        await client.restrict_chat_member(
                            chat_id=message.chat.id,
                            user_id=message.reply_to_message.from_user.id,
                            permissions=mute_permission,
                            until_date=int(time.time() + 86400)
                        )
                        await message.edit(
                            f"<b>Лишен права голоса на 24 часа</b>\n"
                            f"<b>Пользователь: <a href='tg://user?id={get_mem.user.id}'>{get_mem.user.first_name}</a></b>"
                            f"<b>({get_mem.user.id})</b>\n"
                            f"<b>В чате: {get_group.title} ({chat_id})</b>",
                            parse_mode='HTML')
                    else:
                        await client.restrict_chat_member(
                            chat_id=message.chat.id,
                            user_id=message.reply_to_message.from_user.id,
                            permissions=mute_permission
                        )
                        await message.edit(
                            f"<b>Лишен права голоса навсегда</b>\n"
                            f"<b>Пользователь: <a href='tg://user?id={get_mem.user.id}'>{get_mem.user.first_name}</a></b></b>"
                            f"<b>({get_mem.user.id})</b>\n"
                            f"<b>В чате: {get_group.title} ({chat_id})</b>",
                            parse_mode='HTML')
                except Exception as e:
                    await message.edit(
                        f"<b>{e}</b>",
                        parse_mode='HTML')
                    return
            else:
                await message.edit("<b>Не у кого лишать права голоса</b>", parse_mode='HTML')
                await asyncio.sleep(5)
                await message.delete()
        else:
            await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
    else:
        await message.delete()


@Client.on_message(filters.command(["unmute"], prefix) & filters.me)
async def unmute(client, message):
    if message.chat.type in ['group', 'supergroup']:
        chat_id = message.chat.id
        get_group = await client.get_chat(chat_id)
        can_unmute = await admin_check(message)
        if can_unmute:
            try:
                if message.reply_to_message:
                    get_mem = await client.get_chat_member(
                        chat_id,
                        message.reply_to_message.from_user.id
                    )
                    await client.restrict_chat_member(
                        chat_id=message.chat.id,
                        user_id=message.reply_to_message.from_user.id,
                        permissions=unmute_permissions
                    )
                    await message.edit(
                        f"<b>Теперь этот пользователь может говорить</b>\n"
                        f"<b>Пользователь: <a href='tg://user?id={get_mem.user.id}'>{get_mem.user.first_name}</a></b></b>"
                        f"<b>({get_mem.user.id})</b>\n"
                        f"<b>В чате: {get_group.title} ({chat_id})</b>",
                        parse_mode='HTML')
                else:
                    await message.edit("<b>Не кому возвращать права голоса</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
            except Exception as e:
                await message.edit(
                    f"<b>{e}</b>",
                    parse_mode='HTML')
                return
        else:
            await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
    else:
        await message.delete()


@Client.on_message(filters.command(["purge"], prefix) & filters.me)
async def purge_message(client, message):
    await message.delete()
    message_ids = []
    if message.reply_to_message:
        for a_s_message_id in range(message.reply_to_message.message_id, message.message_id):
            message_ids.append(a_s_message_id)
            if len(message_ids) == 100:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=message_ids,
                    revoke=True
                )
                message_ids = []
        if len(message_ids) > 0:
            await client.delete_messages(
                chat_id=message.chat.id,
                message_ids=message_ids,
                revoke=True
            )
    msg = await client.send_message(
        message.chat.id,
        f"<b>Cообщения удалены.</b>",
        parse_mode='HTML')
    await asyncio.sleep(1.20)
    await msg.delete()


@Client.on_message(filters.command(["kick"], prefix) & filters.me)
async def kick(client, message):
    if message.chat.type in ['group', 'supergroup']:
        chat_id = message.chat.id
        get_group = await client.get_chat(chat_id)
        can_kick = await admin_check(message)
        if can_kick:
            if message.reply_to_message:

                try:
                    get_mem = await client.get_chat_member(
                        chat_id,
                        message.reply_to_message.from_user.id
                    )
                    await client.kick_chat_member(chat_id, get_mem.user.id)
                    await client.unban_chat_member(chat_id, get_mem.user.id)
                    await message.edit(
                        f"<b>Пользователь кикнут</b>\n"
                        f"<b>Пользователь: <a href='tg://user?id={get_mem.user.id}'>{get_mem.user.first_name}</a></b></b>\n"
                        f"<b>({get_mem.user.id})</b>\n"
                        f"<b>В чате: {get_group.title} ({chat_id})</b>",
                        parse_mode='HTML')

                except ChatAdminRequired:
                    await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except Exception as e:
                    await message.edit(
                        f"<b>{e}</b>",
                        parse_mode='HTML')
                    return

            else:
                await message.edit("<b>Не кого кикать из чата</b>", parse_mode='HTML')
                await asyncio.sleep(5)
                await message.delete()
                return

        else:
            await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
    else:
        await message.delete()


@Client.on_message(filters.command(["ban"], prefix) & filters.me)
async def ban(client, message):
    if message.chat.type in ['group', 'supergroup']:
        chat_id = message.chat.id
        get_group = await client.get_chat(chat_id)
        can_ban = await admin_check(message)

        if can_ban:
            if message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
            else:
                await message.edit("<b>Не кого банить.</b>", parse_mode='HTML')
                await asyncio.sleep(5)
                await message.delete()

            if user_id:
                try:
                    get_mem = await client.get_chat_member(chat_id, user_id)
                    await client.kick_chat_member(chat_id, user_id)
                    await message.edit(
                        f"<b>Пользователь Заблокирован</b>\n"
                        f"<b>Пользователь: <a href='tg://user?id={get_mem.user.id}'>{get_mem.user.first_name}</a></b></b>\n"
                        f"<b>({get_mem.user.id})</b>\n"
                        f"<b>В чате: {get_group.title} ({chat_id})</b>",
                        parse_mode='HTML')

                except UsernameInvalid:
                    await message.edit("<b>Неверный юзернейм</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except PeerIdInvalid:
                    await message.edit("<b>Неверный юзернейм или айди</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except UserIdInvalid:
                    await message.edit("<b>Неверныое айди</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except ChatAdminRequired:
                    await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except Exception as e:
                    await message.edit(f"<b>{e}</b>", parse_mode='HTML')
                    return

        else:
            await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
            return
    else:
        await message.delete()


@Client.on_message(filters.command(["unban"], prefix) & filters.me)
async def unban(client, message):
    if message.chat.type in ['group', 'supergroup']:
        chat_id = message.chat.id
        get_group = await client.get_chat(chat_id)
        can_unban = await admin_check(message)
        if can_unban:
            if message.reply_to_message:
                try:
                    get_mem = await client.get_chat_member(
                        chat_id,
                        message.reply_to_message.from_user.id
                    )
                    await client.unban_chat_member(chat_id, get_mem.user.id)
                    await message.edit(
                        f"<b>Пользователь Разблокирован</b>\n"
                        f"<b>Пользователь: <a href='tg://user?id={get_mem.user.id}'>{get_mem.user.first_name}</a></b></b>\n"
                        f"<b>({get_mem.user.id})</b>\n"
                        f"<b>В чате: {get_group.title} ({chat_id})</b>",
                        parse_mode='HTML')

                except Exception as e:
                    await message.edit(f"<b>{e}</b>", parse_mode='HTML')
                    return

            else:
                await message.edit("<b>Не кого разбанить.</b>", parse_mode='HTML')
                await asyncio.sleep(5)
                await message.delete()
                return
        else:
            await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
    else:
        await message.delete()


@Client.on_message(filters.command(["promote"], prefix) & filters.me)
async def promote(client, message):
    if message.chat.type in ['group', 'supergroup']:
        cmd = message.command
        custom_rank = ""
        chat_id = message.chat.id
        get_group = await client.get_chat(chat_id)
        can_promo = await is_sudoadmin(message)

        if can_promo:
            if message.reply_to_message:
                get_mem = await client.get_chat_member(
                    chat_id,
                    message.reply_to_message.from_user.id
                )
                user_id = message.reply_to_message.from_user.id
                custom_rank = get_emoji_regexp().sub(u'', " ".join(cmd[1:]))

                if len(custom_rank) > 15:
                    custom_rank = custom_rank[:15]
            else:
                await message.edit("<b>Не кого повышать в правах.</b>", parse_mode='HTML')
                await asyncio.sleep(5)
                await message.delete()
                return

            if user_id:
                try:
                    await client.promote_chat_member(chat_id, user_id,
                                                     can_change_info=True,
                                                     can_delete_messages=True,
                                                     can_restrict_members=True,
                                                     can_invite_users=True,
                                                     can_pin_messages=True)

                    await asyncio.sleep(2)
                    await client.set_administrator_title(chat_id, user_id, custom_rank)
                    await message.edit(
                        f"<b>Пользователь стал админом!</b>\n"
                        f"<b>Пользователь: <a href='tg://user?id={get_mem.user.id}'>{get_mem.user.first_name}</a></b></b>\n"
                        f"<b>({get_mem.user.id})</b>\n"
                        f"<b>В чате: {get_group.title} ({chat_id})</b>",
                        parse_mode='HTML')

                except UsernameInvalid:
                    await message.edit("<b>Неверный юзернейм</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except PeerIdInvalid:
                    await message.edit("<b>Неверный юзернейм или айди</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except UserIdInvalid:
                    await message.edit("<b>Неверныое айди</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except ChatAdminRequired:
                    await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except Exception as e:
                    await message.edit(f"<b>{e}</b>", parse_mode='HTML')
                    return

        else:
            await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
    else:
        await message.delete()


@Client.on_message(filters.command(["demote"], prefix) & filters.me)
async def demote(client, message):
    if message.chat.type in ['group', 'supergroup']:
        chat_id = message.chat.id
        get_group = await client.get_chat(chat_id)
        can_demote = await is_sudoadmin(message)

        if can_demote:
            if message.reply_to_message:
                try:
                    get_mem = await client.get_chat_member(
                        chat_id,
                        message.reply_to_message.from_user.id
                    )
                    await client.promote_chat_member(chat_id, get_mem.user.id,
                                                     can_change_info=False,
                                                     can_delete_messages=False,
                                                     can_restrict_members=False,
                                                     can_invite_users=False,
                                                     can_pin_messages=False)

                    await message.edit(
                        f"<b>Пользователь больше не админ!</b>\n"
                        f"<b>Пользователь: <a href='tg://user?id={get_mem.user.id}'>{get_mem.user.first_name}</a></b></b>"
                        f"<b>({get_mem.user.id})</b>\n"
                        f"<b>В чате: {get_group.title} ({chat_id})</b>",
                        parse_mode='HTML')
                except ChatAdminRequired:
                    await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except Exception as e:
                    await message.edit(f"<b>{e}</b>", parse_mode='HTML')
                    return

            if not message.reply_to_message:
                await message.edit("<b>Не кого унижать в правах.</b>", parse_mode='HTML')
                return
        else:
            await message.edit("<b>Нет прав.</b>", parse_mode='HTML')
    else:
        await message.delete()


@Client.on_message(filters.command(["lock"], prefix) & filters.me)
async def lock(client, message):
    if message.chat.type in ['group', 'supergroup']:
        cmd = message.command
        is_admin = await admin_check(message)
        if not is_admin:
            await message.delete()
            return
        msg = ""
        media = ""
        stickers = ""
        animations = ""
        games = ""
        inlinebots = ""
        webprev = ""
        polls = ""
        info = ""
        invite = ""
        pin = ""
        perm = ""
        lock_type = " ".join(cmd[1:])
        chat_id = message.chat.id
        if not lock_type:
            await message.edit("<b>Мне нечего блокировать.</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
            return

        get_perm = await client.get_chat(chat_id)

        msg = get_perm.permissions.can_send_messages
        media = get_perm.permissions.can_send_media_messages
        stickers = get_perm.permissions.can_send_stickers
        animations = get_perm.permissions.can_send_animations
        games = get_perm.permissions.can_send_games
        inlinebots = get_perm.permissions.can_use_inline_bots
        webprev = get_perm.permissions.can_add_web_page_previews
        polls = get_perm.permissions.can_send_polls
        info = get_perm.permissions.can_change_info
        invite = get_perm.permissions.can_invite_users
        pin = get_perm.permissions.can_pin_messages

        if lock_type == "all":
            try:
                await client.set_chat_permissions(chat_id, ChatPermissions())
                await message.edit("<b>Чат заблокирован.</b>", parse_mode='HTML')
                await asyncio.sleep(5)
                await message.delete()

            except Exception as e:
                await message.edit(
                    text=f"<b>{e}</b>", parse_mode='HTML')

            return

        if lock_type == "msg":
            msg = False
            perm = "messages"

        elif lock_type == "media":
            media = False
            perm = "audios, documents, photos, videos, video notes, voice notes"

        elif lock_type == "stickers":
            stickers = False
            perm = "stickers"

        elif lock_type == "animations":
            animations = False
            perm = "animations"

        elif lock_type == "games":
            games = False
            perm = "games"

        elif lock_type == "inlinebots":
            inlinebots = False
            perm = "inline bots"

        elif lock_type == "webprev":
            webprev = False
            perm = "web page previews"

        elif lock_type == "polls":
            polls = False
            perm = "polls"

        elif lock_type == "info":
            info = False
            perm = "info"

        elif lock_type == "invite":
            invite = False
            perm = "invite"

        elif lock_type == "pin":
            pin = False
            perm = "pin"

        else:
            await message.edit("<b>Неверный элемент для блокировки</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
            return

        try:
            await client.set_chat_permissions(chat_id,
                                              ChatPermissions(can_send_messages=msg,
                                                              can_send_media_messages=media,
                                                              can_send_stickers=stickers,
                                                              can_send_animations=animations,
                                                              can_send_games=games,
                                                              can_use_inline_bots=inlinebots,
                                                              can_add_web_page_previews=webprev,
                                                              can_send_polls=polls,
                                                              can_change_info=info,
                                                              can_invite_users=invite,
                                                              can_pin_messages=pin))

            await message.edit(text=f"<b>Права {perm} заблокированы в этом чате</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()

        except Exception as e:
            await message.edit(
                f"<b>{e}</b>", parse_mode="HTML")
    else:
        await message.delete()


@Client.on_message(filters.command(["unlock"], prefix) & filters.me)
async def unlock(client, message):
    if message.chat.type in ['group', 'supergroup']:
        cmd = message.command
        is_admin = await admin_check(message)
        if not is_admin:
            await message.delete()
            return

        umsg = ""
        umedia = ""
        ustickers = ""
        uanimations = ""
        ugames = ""
        uinlinebots = ""
        uwebprev = ""
        upolls = ""
        uinfo = ""
        uinvite = ""
        upin = ""
        uperm = ""  # pylint:disable=E0602

        unlock_type = " ".join(cmd[1:])
        chat_id = message.chat.id

        if not unlock_type:
            await message.edit("<b>Мне нечего разблокировать.</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
            return

        get_uperm = await client.get_chat(chat_id)

        umsg = get_uperm.permissions.can_send_messages
        umedia = get_uperm.permissions.can_send_media_messages
        ustickers = get_uperm.permissions.can_send_stickers
        uanimations = get_uperm.permissions.can_send_animations
        ugames = get_uperm.permissions.can_send_games
        uinlinebots = get_uperm.permissions.can_use_inline_bots
        uwebprev = get_uperm.permissions.can_add_web_page_previews
        upolls = get_uperm.permissions.can_send_polls
        uinfo = get_uperm.permissions.can_change_info
        uinvite = get_uperm.permissions.can_invite_users
        upin = get_uperm.permissions.can_pin_messages

        if unlock_type == "all":
            try:
                await client.set_chat_permissions(chat_id,
                                                  ChatPermissions(can_send_messages=True,
                                                                  can_send_media_messages=True,
                                                                  can_send_stickers=True,
                                                                  can_send_animations=True,
                                                                  can_send_games=True,
                                                                  can_use_inline_bots=True,
                                                                  can_send_polls=True,
                                                                  can_change_info=True,
                                                                  can_invite_users=True,
                                                                  can_pin_messages=True,
                                                                  can_add_web_page_previews=True))

                await message.edit("<b>Чат разблокирован.</b>", parse_mode='HTML')
                await asyncio.sleep(5)
                await message.delete()

            except Exception as e:
                await message.edit(
                    f"<b>{e}</b>", parse_mode='HTML')
            return

        if unlock_type == "msg":
            umsg = True
            uperm = "messages"

        elif unlock_type == "media":
            umedia = True
            uperm = "audios, documents, photos, videos, video notes, voice notes"

        elif unlock_type == "stickers":
            ustickers = True
            uperm = "stickers"

        elif unlock_type == "animations":
            uanimations = True
            uperm = "animations"

        elif unlock_type == "games":
            ugames = True
            uperm = "games"

        elif unlock_type == "inlinebots":
            uinlinebots = True
            uperm = "inline bots"

        elif unlock_type == "webprev":
            uwebprev = True
            uperm = "web page previews"

        elif unlock_type == "polls":
            upolls = True
            uperm = "polls"

        elif unlock_type == "info":
            uinfo = True
            uperm = "info"

        elif unlock_type == "invite":
            uinvite = True
            uperm = "invite"

        elif unlock_type == "pin":
            upin = True
            uperm = "pin"

        else:
            await message.edit("<b>Неверный элемент для разблокировки</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()
            return

        try:
            await client.set_chat_permissions(chat_id,
                                              ChatPermissions(can_send_messages=umsg,
                                                              can_send_media_messages=umedia,
                                                              can_send_stickers=ustickers,
                                                              can_send_animations=uanimations,
                                                              can_send_games=ugames,
                                                              can_use_inline_bots=uinlinebots,
                                                              can_add_web_page_previews=uwebprev,
                                                              can_send_polls=upolls,
                                                              can_change_info=uinfo,
                                                              can_invite_users=uinvite,
                                                              can_pin_messages=upin))

            await message.edit(f"<b> Права {uperm} разблокированны в этом чате.</b>", parse_mode='HTML')
            await asyncio.sleep(5)
            await message.delete()

        except Exception as e:
            await message.edit(
                f"<b>{e}</b>", parse_mode='HTML')
    else:
        await message.delete()


@Client.on_message(filters.command(["vlock"], prefix) & filters.me)
async def vlock(client, message):
    if message.chat.type in ['group', 'supergroup']:
        chat_id = message.chat.id
        get_group = await client.get_chat(chat_id)
        is_admin = await admin_check(message)
        if not is_admin:
            await message.delete()
            return

        v_perm = ""
        vmsg = ""
        vmedia = ""
        vstickers = ""
        vanimations = ""
        vgames = ""
        vinlinebots = ""
        vwebprev = ""
        vpolls = ""
        vinfo = ""
        vinvite = ""
        vpin = ""

        v_perm = await client.get_chat(message.chat.id)

        def convert_to_emoji(val: bool):
            if val is True:
                return "Разрешено"
            return "Запрещено"

        vmsg = convert_to_emoji(v_perm.permissions.can_send_messages)
        vmedia = convert_to_emoji(v_perm.permissions.can_send_media_messages)
        vstickers = convert_to_emoji(v_perm.permissions.can_send_stickers)
        vanimations = convert_to_emoji(v_perm.permissions.can_send_animations)
        vgames = convert_to_emoji(v_perm.permissions.can_send_games)
        vinlinebots = convert_to_emoji(v_perm.permissions.can_use_inline_bots)
        vwebprev = convert_to_emoji(v_perm.permissions.can_add_web_page_previews)
        vpolls = convert_to_emoji(v_perm.permissions.can_send_polls)
        vinfo = convert_to_emoji(v_perm.permissions.can_change_info)
        vinvite = convert_to_emoji(v_perm.permissions.can_invite_users)
        vpin = convert_to_emoji(v_perm.permissions.can_pin_messages)

        if v_perm is not None:
            try:
                permission_view_str = ""

                permission_view_str += f"<b>Права чата: {get_group.title} ({chat_id})</b>\n"
                permission_view_str += f"<b>Отправка сообщений: {vmsg}</b>\n"
                permission_view_str += f"<b>Отправка медиа: {vmedia}</b>\n"
                permission_view_str += f"<b>Отправка стикеров: {vstickers}</b>\n"
                permission_view_str += f"<b>Отправка гиф: {vanimations}</b>\n"
                permission_view_str += f"<b>Отправка игр: {vgames}</b>\n"
                permission_view_str += f"<b>Использование инлайн ботов: {vinlinebots}</b>\n"
                permission_view_str += f"<b>Веб превью: {vwebprev}</b>\n"
                permission_view_str += f"<b>Отправка голосований: {vpolls}</b>\n"
                permission_view_str += f"<b>Изменение информации чата: {vinfo}</b>\n"
                permission_view_str += f"<b>Возможность приглашать юзеров: {vinvite}</b>\n"
                permission_view_str += f"<b>Возможность закреплять сообщения:{vpin}</b>\n"

                await message.edit(permission_view_str)

            except Exception as e:
                await message.edit(
                    text=
                    f"<b>{e}</b>", parse_mode='HTML')
    else:
        await message.delete()


@Client.on_message(filters.command(["report"], prefix) & filters.me)
async def reportadm(client, message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = None
    grup = await client.get_chat(message.chat.id)
    alladmins = client.iter_chat_members(message.chat.id, filter="administrators")
    admin = []
    async for a in alladmins:
        if a.status == "administrator" or a.status == "creator":
            if not a.user.is_bot:
                admin.append(mention_html(a.user.id, "\u200b"))
    if message.reply_to_message:
        if text:
            teks = '{}'.format(text)
        else:
            teks = '<b>{} Доложено админам.</b>'.format(
                mention_html(message.reply_to_message.from_user.id,
                             message.reply_to_message.from_user.first_name))
    else:
        if text:
            teks = '{}'.format(html.escape(text))
        else:
            teks = "<b>Ало, админы {}.</b>".format(grup.title)
    teks += "".join(admin)
    await client.send_message(message.chat.id,
                              teks,
                              reply_to_message_id=ReplyCheck(message),
                              parse_mode="HTML")


@Client.on_message(filters.command(["tagall"], prefix) & filters.me)
async def tag_all_users(client, message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = "Всем привет ❤️"
    kek = client.iter_chat_members(message.chat.id)
    async for a in kek:
        if not a.user.is_bot:
            text += mention_html(a.user.id, "\u200b")
    await client.send_message(message.chat.id,
                              text,
                              reply_to_message_id=ReplyCheck(message),
                              parse_mode="HTML")


@Client.on_message(filters.command(["kickrand"], prefix) & filters.me)
async def kickrand(client, message):
    user = random.choice([x async for x in client.iter_chat_members(message.chat.id)])
    try:
        await client.kick_chat_member(message.chat.id, user.user.id)
        await message.edit(f"<b><a href='tg://user?id={user.user.id}'>{user.user.first_name}</a> кикнут!</b>")
        await client.unban_chat_member(message.chat.id, user.user.id)
    except:
        await message.edit(
            f"<b>Попытка кика этого говнюка была неудачной <a href='tg://user?id={user.user.id}'>{user.user.first_name}</a></b>")


@Client.on_message(filters.command(["delusers"], prefix) & filters.me)
async def delusers(client, message):
    deleted = [x async for x in client.iter_chat_members(message.chat.id) if x.user.is_deleted]
    await message.edit(f"<b>Найден(ы) {len(deleted)} удаленный(ых)  аккаунт(ов) в {message.chat.id}</b>")
    for u in deleted:
        try:
            await client.kick_chat_member(message.chat.id, u.user.id, int(time.time() + 60))
        except FloodWait as e:
            time.sleep(e.x)


@Client.on_message(filters.command(["kickall"], prefix) & filters.me)
async def kickall(client, message):
    user = [x async for x in client.iter_chat_members(message.chat.id) if x.user]
    await message.edit(f"<b>Будет кикнуто {len(user)}   пользователей из {message.chat.title}</b>")
    for u in user:
        try:
            try:
                await client.kick_chat_member(message.chat.id, u.user.id, int(time.time() + 60))
                await client.unban_chat_member(message.chat.id, u.user.id)
            except:
                pass
        except FloodWait as e:
            time.sleep(e.x)


@Client.on_message(filters.command(["kickme"], prefix) & filters.me)
async def kickme(client, message):
    text = message.text.split(" ", maxsplit=1)[1]
    await message.edit(
        f"<b>Пользователь покинул чат {message.chat.title}\n\nПричина: {text}</b>")
    await client.leave_chat(message.chat.id)


@Client.on_message(filters.command(["adduser"], prefix) & filters.me)
async def adduser(client, message):
    textids = message.text.split(" ", maxsplit=1)[1]
    try:
        await client.add_chat_members(message.chat.id, textids)
        await message.edit(f"<b><a href='tg://user?id={textids}'>Пользователь</a> приглашен успешно!</b>")
    except Exception as e:
        await message.edit(f"<b>{e}</b>")


@Client.on_message(filters.command(["addusers"], prefix) & filters.me)
async def addusers(client, message):
    textidschat = message.text.split(" ", maxsplit=1)[1]
    user = [x async for x in client.iter_chat_members(message.chat.id) if x.user]
    await message.edit(f"<b>{len(user)} пользователей были мигрированы из {message.chat.title} в {textidschat}</b>")
    for u in user:
        try:
            try:
                await client.add_chat_members(textidschat, u.user.id)
            except:
                pass
        except FloodWait as e:
            time.sleep(e.x)


@Client.on_message(filters.command(["dialogs"], prefix) & filters.me)
async def dialogs(client, message):
    dialogsall = [x async for x in client.iter_dialogs()]
    await message.edit(f"<b>Количество диалогов: {len(dialogsall)}</b>")
