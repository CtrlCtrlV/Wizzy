# pip install discord.py
# pip install datetime
# pip install requests
# pip install airtable

import os
import asyncio
from utils import *
import discord
botToken = os.environ['BOTTOKEN']
guildID = os.environ['GUILDID']
bot = discord.Client()
vconsole = []
LKE = "Client request reached bot servers, awaiting handle"

@bot.event
async def on_ready():
    bot.get_channel("850712941031325720").send("Wiz is online")
async def on_message(Message):
  msg = Message.content
  
  # more code here


bot.run(botToken)



