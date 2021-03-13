from pyrogram import Client
from pyrogram import filters
from message import ReplyCheck
import matplotlib.pyplot as plt
import mplcyberpunk
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")


@Client.on_message(filters.command(["graph"], prefix) & filters.me)
async def graph(client, message):
    plotone = message.text.split(" ", maxsplit=14)[1]
    plotwo = message.text.split(" ", maxsplit=14)[2]
    plotthree = message.text.split(" ", maxsplit=14)[3]
    plofour = message.text.split(" ", maxsplit=14)[4]
    plotoness = message.text.split(" ", maxsplit=14)[5]
    plotonesss = message.text.split(" ", maxsplit=14)[6]
    plotonessss = message.text.split(" ", maxsplit=14)[7]
    plotones = message.text.split(" ", maxsplit=14)[8]
    plotwos = message.text.split(" ", maxsplit=14)[9]
    plotthrees = message.text.split(" ", maxsplit=14)[10]
    plotfours = message.text.split(" ", maxsplit=14)[11]
    plotfourss = message.text.split(" ", maxsplit=14)[12]
    plotfoursss = message.text.split(" ", maxsplit=14)[13]
    plotfourssss = message.text.split(" ", maxsplit=14)[14]
    events = [plotone, plotwo, plotthree, plofour, plotoness, plotonesss, plotonessss]
    eventstwo = [plotones, plotwos, plotthrees, plotfours, plotfourss, plotfoursss, plotfourssss]
    plt.style.use("cyberpunk")
    plt.plot(events, marker='o')
    plt.plot(eventstwo, marker='o')
    mplcyberpunk.add_glow_effects()
    plt.savefig(fname='cyber.png')
    plt.close()
    await client.send_photo(message.chat.id, 'cyber.png',
                            caption=f"<b>{plotone} {plotwo} {plotthree} {plofour} {plotoness} {plotonesss} {plotonessss} {plotones} {plotwos} {plotthrees} {plotfours} {plotfourss} {plotfoursss} {plotfourssss}</b>",
                            reply_to_message_id=ReplyCheck(message))
    await message.delete()