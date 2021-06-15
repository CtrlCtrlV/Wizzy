# pip install discord.py
# pip install python-dotenv
# pip install datetime
"""
import os
from utils import *
from dotenv import load_dotenv
load_dotenv()
botToken = os.getenv('DISCORDBOTTOKEN')
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