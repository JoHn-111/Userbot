from pyrogram import Client
from pyrogram import filters
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")

@Client.on_message(filters.command(["h"], prefix) & filters.me)
async def h(client, message):
    await message.edit(
        "<b>Userbot @LaciaMemeFrame's"
        "\n\nДоступные модули:"
        "\n\nSystem: <code>restart</code>, <code>ping</code>, <code>eval</code>, <code>terminal</code>, "
        "<code>uptime</code> "
        "\nhelp: <code>h</code>"
        "\nAdmin: <code>pin</code>, <code>del</code>, <code>mute</code>, <code>unmute</code>, <code>purge</code>, "
        "<code>kick</code>, <code>ban</code>, <code>unban</code>,  <code>promote</code>,  <code>demote</code>,  "
        "<code>lock</code>,  <code>unlock</code>,  <code>vlock</code>, <code>report</code>, <code>tagall</code>, "
        "<code>kickrand</code>, <code>delusers</code>,<code>kickall</code> <code>kickme</code>, "
        "<code>adduser</code>, <code>addusers</code>, <code>dialogs</code> "
        "\nMems18+AHahhaha: <code>f</code>, <code>heart</code>"
        "\nspam: <code>spam</code>, <code>hentaispam</code>"
        "\nlastfmrobot: <code>lastfm</code>"
        "\nQuotLyBot: <code>quote</code>"
        "\nhentai: <code>2dnudes</code>"
        "\nDownloadFiles: <code>filesd</code>, <code>filesu</code>"
        "\nchat_id: <code>idchat</code>"
        "\nwhois: <code>whois</code>"
        "\npentesting: <code>pentesting</code>, <code>copy</code>"
        "\nText-to-Speech: <code>tts</code>"
        "\nGif Tenor & Giphy: <code>tenor</code>, <code>giphy</code>"
        "\nGraph: <code>graph</code>\nPermalink: <code>permalink</code>"
        f"\n\nCommand-Prefix: <code>{prefix}</code>"
        "\n\nВерсия: <code>1.0</code>"
        "\n<a href='https://pyrogram.org'>Больше информации</a></b>",
        parse_mode='HTML', disable_web_page_preview=True)
