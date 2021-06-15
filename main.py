# pip install discord.py
# pip install datetime
"""
import os
from utils import *
botToken = os.environ['BOTTOKEN']
bot = discord.Client()
vconsole = []

@bot.event
async def on_message(Message):
  msg = Message.content
  def send(message):
    msg.channel.send(message)
  print("Message received"+msg)
  send("Hello")
  # more code here



bot.run(botToken)
"""


