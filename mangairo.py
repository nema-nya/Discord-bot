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

def first_chapter(mangaid):
    manga_url = f"https://mangairo.com/series-{mangaid}"
    response = requests.get(manga_url)
    soup = bs4.BeautifulSoup(response.content, features="html.parser")
    for li in soup.find_all("li"):
        if li.span is None:
            continue
        if li.span.string == "Read First Chapter : ":
            return li.a.string.split()[1]

def max_chapters(mangaid):
    manga_url = f"https://mangairo.com/series-{mangaid}"
    response = requests.get(manga_url)
    soup = bs4.BeautifulSoup(response.content, features="html.parser")
    for li in soup.find_all("li"):
        if li.span is None:
            continue
        if li.span.string == "Read Latest Chapter : ":
            return li.a.string.split()[2]

def get_manga_soup(mangaid, chapter):
    manga_url = f"https://mangairo.com/series-{mangaid}/chapter-{chapter}"
    response = requests.get(manga_url)
    return bs4.BeautifulSoup(response.content, features="html.parser")

def get_manga_pages(soup):
    pages = []
    for page in soup.find_all("img", "img_content"):
        pages.append(page["src"])
    if len(pages) == 0:
        return None
    else:
        return pages
