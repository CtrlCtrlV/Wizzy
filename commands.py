import db
import plugins

async def tap(args, msObject):
    await msObject.channel.send(args)

async def add(args,msObject):
    # declare all variables
    taskName  = ""
    dueDate = ""
    assignDate = ""
    lis = ""
    tagsArr = []
    tagsStr = ""
    priority = 1
    notes = ""
    # "myTask her Name" due 13June assign 10June $inbox tag1;tag2;tag3 notes:my notes go here P1
    nameState = False
    taskName = ""
    for i in args:
        if '"' in i and nameState == False:
            nameState = True
            taskName += i.replace('"',"")
        elif '"' in i and nameState == True:
            nameState = False
            taskName += " " +i.replace('"', "")
        elif nameState == True and '"' not in i:
            taskName += " "+i
    # taskName
    itr = 0
    for i in args:
        itr +=1
        if i=="due":
            dueDate = args[itr+2]
    # dueDate
    itr = 0
    for i in args:
        itr += 1
        if i=="assign":
            assignDate = args[itr+2]
    # assignDate
    for i in args:
        if "$" in i:
            lis = i.replace("$","")
    # lis
    for i in args:
        if ";" in i:
            tagsArr = i.split(";")
            tagsStr = ";".join(tagsArr)
    # tagsArr tagsStr 
    for i in args:
        if "P" in i:
            priority = i.replace("P","")
    # priority
    noteState = False
    notes = ""
    for i in args:
        if i.lower()=="notes:":
            noteState = True
        elif noteState == True:
            notes += " " + i
    # notes
    taskObject = {
        "name":taskName,
        "dueDate": dueDate,
        "assignedDate": assignDate,
        "tags":tagsArr,
        "list": lis,
        "priority": int(priority),
        "notes":notes
    }
    return taskObject



