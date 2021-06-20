from datetime import date
vconsole = []
def log(text, flag=""):
  now = date.today()
  timestamp = now.strftime("%H:%M:%S >> ")
  
  if flag =="":
        vconsole.append(str(timestamp)+str(text))
  elif flag=="w":
        vconsole.append(str(timestamp)+":warning: "+str(text))
  elif flag=="e":
        vconsole.append(str(timestamp)+":no_entry: "+str(text))
  else:
      vconsole.append(str(timestamp)+":gear: "+str(text))
    

def error(title, msg,where,fix):
    construct ="""
|=========
| ERROR  |
|=========

**{}**

> {}

{}

To fix this issue:
{}
""".format(title, where,msg,fix)
    return construct