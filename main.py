# pip install discord.py
# pip install datetime
# pip install requests
# pip install airtable

import os
import utils
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
    async def send(sendMessage):
        if type(sendMessage['msg']) is list:
            for i in sendMessage['msg']:
                Message.channel.send(i)
        elif type(sendMessage['msg']) is str:
            Message.channel.send(sendMessage['msg'])
        # postProcesseses

    if Message.author == bot.user:
        return

    msg = Message.content
    incomingRaw = msg
    incomingRawArr = msg.split(" ")

    if incomingRaw.startswith("wiz") or incomingRaw.startswith("orto"):
        del incomingRawArr[0]
    else:
        return

    root = incomingRawArr[0]
    if root=="thankyou" or root=="thank":
        await send({"msg":"You're Welcome!"})
    if root == "tap":
        del incomingRawArr[0]
        await send(commands.tap(" ".join(incomingRawArr), Message))
    elif root=="add":
        del incomingRawArr[0]
        await send(commands.addTask(incomingRawArr, Message))
    elif root=="remember":
        del incomingRawArr[0]
        await send(commands.addEvent(incomingRawArr, Message))
    elif root=="show":
        if incomingRawArr[1]=="tasks":
            if incomingRawArr[2]=="$due":
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
        await send({'msg':str(utils.error('Invalid Root','The root used "'+str(root)+'" is invalid (does not exist).','main.py >> root handler','Read the docs for more information, or check your plugin documentation if you have attempted to command a plugin'))})
        # need smarter error handling such as checking if a plugin was used
    
######################################    

bot.run(botToken)



