def runFirstInstallScript(msObject):
    async def send(message):
        await msObject.channel.send(message)
    await send("""Hey, there! I'm Wiz, your personal assistant. Let's setup some stuff, shall we?
    """)
    await send("""
-----------
1 of 3
-----------
Firstly, could you help fill out this form? Just copy and paste with the responses filled out. 
If your answer is no, just leave the answer area blank.
Thanks!

1. Do you have a dedicated text channel for Wiz only? If yes, please state the channel ID. 
>>

2. How would you like to be addressed? (Default: User)
>>
    """)