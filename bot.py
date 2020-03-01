import discord
import requests
import bs4
import re
import time
import PIL.Image
import io
import math
import random
import json
import os
import time
import mangairo
import builders
import copy
from msgdata import MessageData as MessageData
from reactions import handlers

client = discord.Client()
messages = {}

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!mangairo"):
        channel = message.channel
        await channel.trigger_typing()
        try:
            a = message.content.split()[1]
            b = message.content.split()[2]
        except Exception as e:
            await channel.send("!mangairo [manga id] [chapter]")
            print(str(e))
        message_str = message.content
        manga = await builders.build_manga(message.content)
        sent_msg = await channel.send(embed=manga.myEmbeded)
        messages[sent_msg.id] = manga
        await sent_msg.add_reaction(u"\u23ee") #p
        await sent_msg.add_reaction(u"\u27a1") #r

@client.event
async def on_reaction_add(reaction, user):
    global messages
    react_id = reaction.message.id
    react_emoji = reaction.emoji
    data = messages[react_id]	
    if user == client.user:
        return
    if react_id in messages:
        await handlers[react_emoji](reaction, data)
        

client.run("")

