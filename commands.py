import db
import plugins
from utils import *
from datetime import datetime
import dateparser 

async def tap(args, msObject):
    await msObject.channel.send(args)

async def addTask(args,msObject):
    log("beginning command execution")
    # declare all variables
    taskName  = ""
    dueDate = ""
    assignDate = ""
    lis = ""
    tagsArr = []
    tagsStr = ""
    priority = 1
    notes = ""
    log("   |- context vars loaded > success")
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
    log("   |- task name parsed successfully")
    # taskName
    itr = 0
    for i in args:
        itr +=1
        if i=="due":
            dueDate = args[itr+2]
    log("   |- due date parsed successfully")
    # dueDate
    itr = 0
    for i in args:
        itr += 1
        if i=="assign":
            assignDate = args[itr+2]
    log("   |- assigned date parsed successfully")
    # assignDate
    for i in args:
        if "$" in i:
            lis = i.replace("$","")
    log("   |- list declaration parsed successfully")
    # lis
    for i in args:
        if ";" in i:
            tagsArr = i.split(";")
            tagsStr = ";".join(tagsArr)
    log("   |- tags parsed successfully")
    # tagsArr tagsStr 
    for i in args:
        if "P" in i:
            priority = i.replace("P","")
    log("   |- priority declaration parsed successfully")
    # priority
    noteState = False
    notes = ""
    for i in args:
        if i.lower()=="notes:":
            noteState = True
        elif noteState == True:
            notes += " " + i
    log("   |- notes parsed successfully")
    # notes
    log("|_ bulding task object")
    taskObject = {
        "name":taskName,
        "dueDate": dueDate,
        "assignedDate": assignDate,
        "tags":tagsArr,
        "list": lis,
        "priority": int(priority),
        "notes":notes
    }
    log("task object successfully built")
    return taskObject


async def addEvent(args, msObject):
    log("beginning command execution")
    eventName = ""
    colour = ""
    notes = ""
    dDate = ""
    tme = ""
    nameState = False
    log("   |- context vars loaded > success")
    for i in args:
        if '"' in i and nameState == False:
            nameState = True
            eventName += i.replace('"',"")
        elif '"' in i and nameState == True:
            nameState = False
            eventName += " " +i.replace('"', "")
        elif nameState == True and '"' not in i:
            eventName += " "+i
    log("   |- event name parsed successfully")
    # eventName
    for i in args:
        if "time:" in i:
            tme = int(i.replace('time:',''))
    log("   |- event time parsed successfully")
    # tme
    for i in args:
        if "date:" in i:
            dDate = str(i.replace("date:",""))
            superDate = str(dateparser.parse(dDate).strftime("%d/%m/%Y %H%M"))
        # 13/06/2021 1359
    log("   |- event date time object: standardise > success")
    # superDate
    for i in args:
        if "$" in i:
            colour = i.replace("$","")
    log("   |- colour code parsed successfully")
    # colour
    noteState = False
    for i in args:
        if i.lower()=="notes:":
            noteState = True
        elif noteState == True:
            notes += " " + i
    log("   |- event notes parsed successfully")
    # notes
    log("|_ bulding event object")
    eventObject = {
        "name":eventName,
        "date": str(superDate),
        "time": tme,
        "notes":notes,
        "colour":colour
    }
    log("event object successfully built")
    return eventObject

async def viewAllTasks(args, msObject):
    pass 

async def viewTasksbyDue(args, msObject):
    # get data from database
    unsortedDates = []
    data = [
        {'name': 'event X',
        'date': '18/06/2021 0757',
        'time': 1234,
        'notes':
        ' my notes here',
        'colour': 'red'
        },
        {'name': 'event Y',
        'date': '18/06/2022 0757',
        'time': 1234,
        'notes':
        ' my notes here',
        'colour': 'red'
        },
        {'name': 'event Z',
        'date': '20/06/2021 0757',
        'time': 1234,
        'notes':
        ' my notes here',
        'colour': 'red'
        }
        ]
    for i in data:
        thisDate = i['date']
        unsortedDates.append(thisDate)
    unsortedDates.sort(key = lambda date: datetime.strptime(date, '%d %b %Y'))
    dates =  ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018", 
              "01 Jan 2019", "10 Jul 2016", "01 Jan 2007"]  
      
    # Sort the list in ascending order of dates 
    sortedDates = dates.sort(key = lambda dat: datetime.strptime(dat, '%d/%m/%Y %H%M'))
    print(sortedDates)
    return sortedDates
