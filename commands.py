import db
import plugins

async def tap(args, msObject):
    await msObject.channel.send(args)

async def add(args,msObject):
    # "myTask her Name" due 13June assign 10June $inbox tag1;tag2;tag3 notes:my notes go here P1
    nameState = False
    taskName = ""
    for i in args:
        if i.includes('"') and nameState == False:
            nameState = True
            taskName += i.replace('"',"")
        elif i.includes('"') and nameState == True:
            nameState = False
            taskName += i.replace('"', "")
        elif nameState == True and i.includes('"')==False:
            taskName += " "+i
    await msObject.channel.send(taskName)
