#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests  # lib for going on internet
from bs4 import BeautifulSoup  # html parser
import urllib.parse

def getcomics_top_link(user_input):

    formated_search = urllib.parse.quote_plus(user_input.lower(), safe='', encoding=None, errors=None)
    getcomics_search = f"https://getcomics.info/?s={formated_search}"
    # get HTML page with requests.get
    res = requests.get(getcomics_search)
    res.close()

    # BeautifulSoup will transform raw HTML in a tree easy to parse
    soup = BeautifulSoup(res.text, 'lxml')

    first = soup.find('h1', class_='post-title')

    title = first.text
    url = first.a['href']

    return title,url
