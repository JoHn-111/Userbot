from pyrogram import Client
from pyrogram import filters
import asyncio
import random
from message import ReplyCheck
import configparser
import os
import sys
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
prefix = config.get("pyrogram", "prefix")

sticker_list = ['CAACAgIAAxkBAAEBxLNgAXDpsGlh4CYBtDLulTQ48JMSxQACswADTptkAs5hkxBiRE31HgQ',
                'CAACAgIAAxkBAAEBxLVgAXIJszo0WbCmsVQdZ_XNgPJbrwAC3QADTptkAsbfbuRgzncfHgQ',
                'CAACAgIAAxkBAAEBxLtgAXJdfq6D-pJE8U2hiKMp98GHBgACCwEAAk6bZAKGibEPCbcdaR4E',
                'CAACAgIAAxkBAAEBxL1gAXJvnLGQVzk5W3HuqbSiDxXzEAACHgEAAk6bZAKj35UNnCMgCB4E',
                'CAACAgIAAxkBAAEBxL9gAXJ8QDi_fF6o4szDeI_yNQwaqwACUwEAAk6bZAIaxDzKEZKWUR4E',
                'CAACAgIAAxkBAAEBxMFgAXKHngOXP-qzpk4ogMhDSGOZXAAC2QADTptkAr_7hXFDc9mvHgQ',
                'CAACAgIAAxkBAAEBxMNgAXKlFQ_9R1zaIIDstD0TN_0ldAACrwADTptkAoftMsdli6fnHgQ',
                'CAACAgIAAxkBAAEBxMVgAXK0FY6urGmxLfJU_99JKXZ-rgACtgADTptkAqpNYvdldSrYHgQ',
                'CAACAgIAAxkBAAEBxMdgAXLGtxYEOOP2-4B0EU8HgPwckwACGwEAAk6bZAIif48xqmneWB4E',
                'CAACAgIAAxkBAAEBxMlgAXLQsdJtpwu6RObGT7rM3ddoVAACugADTptkArbrc3oLzTyHHgQ',
                'CAACAgIAAxkBAAEBxMtgAXLexEfezPe2kyLr1dz-usJDTgACuQADTptkAn3O94Pvp3dmHgQ',
                'CAACAgIAAxkBAAEBxM1gAXMERFLyl_Cb4HZFs2QD_0ZgrQACWwEAAk6bZAKfvpp3HJ3Ech4E',
                'CAACAgIAAxkBAAEBxM1gAXMERFLyl_Cb4HZFs2QD_0ZgrQACWwEAAk6bZAKfvpp3HJ3Ech4E',
                'CAACAgIAAxkBAAEBxM9gAXMRCSanstBHBNXe11Tv3MySngACtQADTptkArZTqYEv5ofdHgQ',
                'CAACAgIAAxkBAAEBxNFgAXMc_Qu_V93x5f25ZOomltEiTwACsgADTptkAm1WnTBWvUfiHgQ',
                'CAACAgIAAxkBAAEBxNNgAXMsrCI1kcPNM-UqxBv1eMTsOwACtwADTptkArfi9m2SDIPXHgQ',
                'CAACAgIAAxkBAAEBxNVgAXP_hBpb-WT5Vc9CzYYLT7871wAC2gADTptkAupGXP51-SA0HgQ',
                'CAACAgIAAxkBAAEBxNdgAXQC8UCHTgFPJ9scGkJnpTawkQACswADTptkAs5hkxBiRE31HgQ',
                'CAACAgIAAxkBAAEBxNlgAXQkDd_nmxxLjAfDQG9AulwSIAACDAEAAk6bZAJjkqwbNCLTRx4E',
                'CAACAgIAAxkBAAEBxNtgAXQ-90ZSuBejW0CANG9gjkEf-QACSgEAAk6bZAI3xdjtSHj4UR4E']


@Client.on_message(filters.command(["heart"], prefix) & filters.me)
async def heart(client, message):
    await message.edit("💜")
    await asyncio.sleep(1.1)
    await message.edit("💙")
    await asyncio.sleep(1.1)
    await message.edit("💚")
    await asyncio.sleep(1.1)
    await message.edit("💛")
    await asyncio.sleep(1.1)
    await message.edit("🧡")
    await asyncio.sleep(1.1)
    await message.edit("🖤")
    await asyncio.sleep(1.1)
    await message.edit("💜")
    await asyncio.sleep(1.1)
    await message.edit("💙")
    await asyncio.sleep(1.1)
    await message.edit("💚")
    await asyncio.sleep(1.1)
    await message.edit("💛")
    await asyncio.sleep(1.1)
    await message.edit("🧡")
    await asyncio.sleep(1.1)
    await message.edit("🖤")
    await asyncio.sleep(1.1)


@Client.on_message(filters.command(["f"], prefix) & filters.me)
async def fstik(client, message):
    rand_stick = random.choice(sticker_list)
    await message.reply_sticker(sticker=rand_stick, reply_to_message_id=ReplyCheck(message))
    await message.delete()
