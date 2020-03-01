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
from builders import build_emojis as build_emojis
from builders import build_msg as build_msg
from builders import build_manga as build_manga
from msgdata import MessageData as MessageData
import copy

async def send_reaction_emojis(reaction, data, emojis = []):
    data.myEmbeded.title=builders.build_msg(data, 1)
    data.myEmbeded.set_image(url=data.pages[data.page])
    await reaction.message.edit(embed=data.myEmbeded)
    await reaction.message.clear_reactions()
    for emoji in emojis:
        await reaction.message.add_reaction(emoji)

async def on_left_arrow(reaction, data):
    if reaction.count > 1:
        data.page -= 1
        emojis = build_emojis(data)
        await send_reaction_emojis(reaction, data, emojis)
        
async def on_right_arrow(reaction, data):
    if reaction.count > 1:
        data.page +=1
        emojis = build_emojis(data)
        await send_reaction_emojis(reaction, data, emojis)

async def on_next_arrow(reaction, data):
    if reaction.count > 1:
        message = reaction.message
        discord_message = f"!mangario {str(data.manga_id)} {str(int(data.chapter)+1)}"
        manga = await builders.build_manga(discord_message)
        data.manga_id = manga.manga_id
        data.chapter = manga.chapter
        data.first_chapter = manga.first_chapter
        data.max_chapters = manga.max_chapters
        data.page = manga.page
        data.myEmbeded = manga.myEmbeded
        data.max_page = manga.max_page
        data.pages = manga.pages
        emojis = build_emojis(data)
        await send_reaction_emojis(reaction, data, emojis)

async def on_previous_arrow(reaction, data):
    if reaction.count > 1:
        message = reaction.message
        discord_message = f"!mangario {str(data.manga_id)} {str(int(data.chapter)-1)}"
        manga = await builders.build_manga(discord_message)
        data.manga_id = manga.manga_id
        data.chapter = manga.chapter
        data.first_chapter = manga.first_chapter
        data.max_chapters = manga.max_chapters
        data.page = manga.page
        data.myEmbeded = manga.myEmbeded
        data.max_page = manga.max_page
        data.pages = manga.pages
        emojis = build_emojis(data)
        await send_reaction_emojis(reaction, data, emojis)
        
handlers = {
    u"\u2b05": on_left_arrow,
    u"\u27a1": on_right_arrow,
    u"\u23ed": on_next_arrow,
    u"\u23ee": on_previous_arrow
}

