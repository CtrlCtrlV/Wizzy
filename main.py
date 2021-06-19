# pip install discord.py
# pip install datetime
# pip install requests
# pip install airtable

import os
from utils import *
import discord
import commands
import json
botToken = os.environ['BOTTOKEN']
bot = discord.Client()
import db

# DECLARING MAIN VARIABLES
# vconsole << using from utils.vconsole
LKE = "Client request reached bot servers, awaiting handle"
incomingRaw = ""
incomingRawArr = []
root = ""
thisChannel = 850712941031325720
#####################################

# CREATING EVENTS
@bot.event
async def on_ready():
    await bot.get_channel(thisChannel).send("Wiz is online")
    log("wiz is now online")
    if await db.fetch("versionControl","firstInstall",False)=="True":
        log("checked verscon for firstInstall > false")
        from init import runFirstInstallScript
        for i in await runFirstInstallScript():
            await bot.get_channel(thisChannel).send(i)
        # only update DB first install status after all values are ok
@bot.event
async def on_message(Message):
    log("bot event triggered")
    async def send(sendMessage):
        await Message.channel.send(sendMessage)
        """"
        if type(sendMessage['msg']) is list:
            for i in sendMessage['msg']:
                await Message.channel.send(i)
        elif type(sendMessage['msg']) is str:
            await Message.channel.send(sendMessage['msg'])
        # postProcesseses
        """
    if Message.author == bot.user:
        return

    msg = Message.content
    incomingRaw = msg
    incomingRawArr = msg.split(" ")
    blacklist = [855400651764662282, 745178736982360114, "855400651764662282","745178736982360114"]
    if Message.author.id in blacklist and " -i " not in msg:
        log("ignoring blacklisted user "+str(Message.author.id))
        return
    if incomingRaw.startswith("wiz") or incomingRaw.startswith("orto"):
        del incomingRawArr[0]
    else:
        return

    root = incomingRawArr[0]
    if root=="thankyou" or root=="thank":
        log("valid root '"+root+"' identified")
        await send({"msg":"You're Welcome!"})
    elif root == "tap":
        log("valid root '"+root+"' identified")
        del incomingRawArr[0]
        await send(await commands.tap(" ".join(incomingRawArr), Message))
    elif root=="add":
        log("valid root '"+root+"' identified")
        del incomingRawArr[0]
        await send(commands.addTask(incomingRawArr, Message))
    elif root=="remember":
        log("valid root '"+root+"' identified")
        del incomingRawArr[0]
        await send(commands.addEvent(incomingRawArr, Message))
    elif root=="show":
        log("valid root '"+root+"' identified")
        if incomingRawArr[1]=="tasks":
            log("valid command '"+incomingRawArr[1]+"' identified")
            if incomingRawArr[2]=="$due":
                log("valid arg '"+incomingRawArr[2]+"' identified")
                del incomingRawArr[0]
                del incomingRawArr[0]
                del incomingRawArr[0]
                del incomingRawArr[0]
                await send(commands.viewTasksbyDue(incomingRawArr, Message))
    # DEBUGGING PORT
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
    else:
        log("unkown root '"+root+"' ","e")
        await send({'msg':str(utils.error('Invalid Root','The root used "'+str(root)+'" is invalid (does not exist).','main.py >> root handler','Read the docs for more information, or check your plugin documentation if you have attempted to command a plugin'))})
        # need smarter error handling such as checking if a plugin was used
    log("execution complete")
    # check plugins 
    await send("\n".join(vconsole))
        
    
######################################    

bot.run(botToken)



