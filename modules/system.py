import subprocess
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
import asyncio
import sys
import io
import os
from message import ReplyCheck, restart
from threading import Thread
import configparser

config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["ping"], prefix) & filters.me)
async def ping(client, message):
    from datetime import datetime
    start = datetime.now()
    await message.edit("<b>Pong</b>", parse_mode="HTML")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await asyncio.sleep(0.5)
    await message.edit(f"<b>Понг: {ms}</b>", parse_mode='HTML')


@Client.on_message(filters.command(["eval"], prefix) & filters.me)
async def eval(client, message):
    status_message = await message.reply_text("...", reply_to_message_id=ReplyCheck(message))
    cmd = message.text.split(" ", maxsplit=1)[1]

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Успешно!"

    final_output = "<b>Выражение</b>:\n<code>{}</code>\n\n<b>Вернулось</b>:\n<code>{}</code>\n".format(
        cmd,
        evaluation.strip()
    )

    if len(final_output) > 4096:
        with open("eval.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document="eval.txt",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message)
        )
        os.remove("eval.text")
        await status_message.delete()
    else:
        await status_message.edit(final_output)
        await message.delete()


async def aexec(code, b, m, r):
    sys.tracebacklimit = 0
    exec(
        'async def __aexec(b, m, r): ' +
        ''.join(f'\n {line}' for line in code.split('\n'))
    )
    return await locals()['__aexec'](b, m, r)


@Client.on_message(filters.command(["terminal"], prefix) & filters.me)
async def terminal(_, message: Message):
    cmd = message.text.split(" ", maxsplit=1)[1]
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "Ошибок нету"
    o = stdout.decode()
    if not o:
        o = "Вывода нету"

    OUTPUT = ""
    OUTPUT += f"<b>Команда:\n<code>{cmd}</code></b>\n\n"
    OUTPUT += f"<b>Вывод: \n<code>{o}</code></b>\n"
    OUTPUT += f"\n<b>Ошибки: \n<code>{e}</code></b>"

    if len(OUTPUT) > 4096:
        with open("exec.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(OUTPUT))
        await message.reply_document(
            document="exec.text",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message),
        )
        os.remove("exec.text")
        await message.delete()
    else:
        await message.reply_text(OUTPUT, reply_to_message_id=ReplyCheck(message))
        await message.delete()


@Client.on_message(filters.command(["restart"], prefix) & filters.me)
async def restart_comand(client, message):
    await message.edit("<b>Перезагрузка...</b>")
    Thread(target=restart, args=(client, message)).start()


@Client.on_message(filters.command(["uptime"], prefix) & filters.me)
async def uptime(client, message):
    uptime_print = subprocess.check_output(['uptime'])
    await message.edit(f"<b>{uptime_print}</b>")
