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
    if root=="thankyou" or root=="thank":
        await send("You're Welcome!")
    if root == "tap":
        del incomingRawArr[0]
        await commands.tap(" ".join(incomingRawArr), Message)
    elif root=="add":
        del incomingRawArr[0]
        export = await commands.addTask(incomingRawArr, Message)
        await send(str(export))
    elif root=="remember":
        del incomingRawArr[0]
        export = await commands.addEvent(incomingRawArr, Message)
        await send(str(export))
    elif root=="show":
        if incomingRawArr[1]=="tasks":
            if incomingRawArr[2]=="$due":
                del incomingRawArr[0]
                del incomingRawArr[0]
                del incomingRawArr[0]
                del incomingRawArr[0]
                export = await commands.viewTasksbyDue(incomingRawArr, Message)
                await send(str(export))
    elif root=="db":
        import db
        del incomingRawArr[0]
        if incomingRawArr[0]=="create":
            await db.create('createdKey','Hello')
        elif incomingRawArr[0]=="get":
            await db.fetch('tap', 'tapOn',False)
        elif incomingRawArr[0]=="update":
            await db.update('createdKey', 'updatedValue')
        elif incomingRawArr[0]=="delete":
            await db.destroy('createdKey')
        
######################################    

bot.run(botToken)



