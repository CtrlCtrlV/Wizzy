# pip install discord.py
# pip install datetime
# pip install requests
# pip install airtable

import os
import asyncio
from utils import *
import discord
import commands
botToken = os.environ['BOTTOKEN']
bot = discord.Client()

# DECLARING MAIN VARIABLES
vconsole = []
LKE = "Client request reached bot servers, awaiting handle"
incomingRaw = ""
incomingRawArr = []
root = ""
#####################################

# CREATING EVENTS
@bot.event
async def on_ready():
    await bot.get_channel(850712941031325720).send("Wiz is online")
@bot.event
async def on_message(Message):
    if Message.author == bot.user:
        return
    msg = Message.content
    async def send(sendMessage):
        await Message.channel.send(sendMessage)
    incomingRaw = msg
    incomingRawArr = msg.split(" ")
    if incomingRaw.startswith("wiz") or incomingRaw.startswith("orto"):
        del incomingRawArr[0]
    root = incomingRawArr[0]
    if root == "tap":
        del incomingRawArr[0]
        await commands.tap(" ".join(incomingRawArr), Message)
    elif root=="add":
        del incomingRawArr[0]
        await commands.add(incomingRawArr, Message)
######################################    

bot.run(botToken)



