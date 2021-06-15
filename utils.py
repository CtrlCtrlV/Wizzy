from datetime import date
vconsole = []
def log(text):
  now = date.today()
  timestamp = now.strftime("%H:%M:%S >> ")
  vconsole.append(str(timestamp)+str(text))
