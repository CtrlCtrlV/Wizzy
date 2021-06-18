from datetime import date
vconsole = []
def log(text):
  now = date.today()
  timestamp = now.strftime("%H:%M:%S >> ")
  vconsole.append(str(timestamp)+str(text))
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