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
    log("verscon checking for updates")
    if await db.fetch("versionControl","firstInstall",False)=="True":
        log("checked verscon for firstInstall > true")
        log("@verscon running firstInstall script","w")
        from init import runFirstInstallScript
        for i in await runFirstInstallScript():
            await bot.get_channel(thisChannel).send(i)
        log("@verscon firstInstall script > success")
    else:
        log("checked verscon for firstInstall > false")
        # only update DB first install status after all values are ok
@bot.event
async def on_message(Message):
    async def hypersend(sendMsg):
        await Message.channel.send(sendMsg['msg'])
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
    # deleted
    if incomingRaw.startswith("wiz") or incomingRaw.startswith("orto"):
        log("bot event triggered")
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
        del incomingRawArr[0]
        if incomingRawArr[1]=="tasks":
            del incomingRawArr[0]
            if incomingRawArr=[]:
                await commands.taskOverview(incomingRawArr, Message)
            log("valid command '"+incomingRawArr[1]+"' identified")
            elif incomingRawArr[0]=="$due":
                log("valid arg '"+incomingRawArr[0]+"' identified")
                del incomingRawArr[0]
                await send(commands.viewTasksbyDue(incomingRawArr, Message))
            else:
                # error

    # DEBUGGING PORT
    elif root=="db":
        del incomingRawArr[0]
        if incomingRawArr[0]=="create":
            await db.create('createdKey','Hello')
        elif incomingRawArr[0]=="get":
            await db.fetch('tap', 'tapOn',False)
        elif incomingRawArr[0]=="update":
            await db.update('createdKey', 'updatedValue')
        elif incomingRawArr[0]=="delete":
            await db.destroy('createdKey')
    elif root=="complete":
        del incomingRawArr[0]
        commands.completeTask(incomingRawArr, Messsage)
    else:
        log("unkown root '"+root+"' ","e")
        await hypersend({'msg':str(error('Invalid Root','The root used "'+str(root)+'" is invalid (does not exist).','main.py >> root handler','Read the docs for more information, or check your plugin documentation if you have attempted to command a plugin'))})
        # need smarter error handling such as checking if a plugin was used
    log("execution complete")
    # check plugins 
    print("\n".join(vconsole))
    await send("VIRTUAL CONSOLE:")
    await send("\n".join(vconsole))
        
    
######################################    

bot.run(botToken)



