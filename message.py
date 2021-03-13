import html
from pyrogram.types import Message


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id


async def admin_check(message: Message) -> bool:
    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    admin_strings = [
        "creator",
        "administrator"
    ]
    if check_status.status not in admin_strings:
        return False
    else:
        return True


async def is_sudoadmin(message: Message) -> bool:
    client = message._client
    check_user = await client.get_chat_member(message.chat.id, message.from_user.id)
    user_type = check_user.status
    if user_type == "member":
        return False
    if user_type == "administrator":
        add_adminperm = check_user.can_promote_members
        if add_adminperm:
            return True
        return False
    return True


def mention_html(user_id, name):
    return u'<a href="tg://user?id={}">{}</a>'.format(user_id, html.escape(name))


def restart(client, message):
    client.restart()
    message.edit("<b>UserBot перезагружен!</b>")
