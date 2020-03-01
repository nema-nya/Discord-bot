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
from msgdata import MessageData as MessageData


async def build_manga(message):
    pages = []
    manga_id = message.split()[1]
    chapter = message.split()[2]
    soup = mangairo.get_manga_soup(manga_id, chapter)
    pages = mangairo.get_manga_pages(soup)
    if pages is None:
        await channel.send("I didnt find that")
    current_page = 0
    max_pages = len(pages)
    max_chapters = mangairo.max_chapters(message.split()[1])
    first_chapter = mangairo.first_chapter(manga_id)
    myEmbeded = discord.Embed(title=f"Page: [{current_page+1}/{max_pages}] Chapter: [{chapter}/{max_chapters}]")
    myEmbeded = myEmbeded.set_image(url=pages[0])
    return_msgdata = MessageData(manga_id, chapter, first_chapter, max_chapters, current_page, max_pages, myEmbeded, pages)
    return return_msgdata

def build_emojis(data):
    emojis = []
    if data.chapter != data.first_chapter and data.page == 0:
        emojis.append(u"\u23ee") #prev
    if data.page == 0:
        emojis.append(u"\u27a1") #right
    elif data.page == data.max_page - 1:
        emojis.append(u"\u2b05") #left
    else:
        emojis.append(u"\u2b05") #l
        emojis.append(u"\u27a1") #r
    if data.chapter != data.max_chapters and data.page == data.max_page - 1:
        emojis.append(u"\u23ed") #next
    return emojis

def build_msg(data, page_inc):
    return f"Page: [{data.page+page_inc}/{data.max_page}] Chapter: [{data.chapter}/{data.max_chapters}]"