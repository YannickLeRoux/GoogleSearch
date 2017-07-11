#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 19:38:06 2017

@author: yannickleroux

The purpose of this programm is to parse the html of a Mixcloud podcast,
extract the tracklist text using RegEx and find possible download links 
of the different songs using Zippyshare and a Google Search

"""
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import webbrowser


MY_URL = 'http://www.mixcloud.com/hakkasan/hakkasan-deep-podcast-027/'

html = urlopen(MY_URL)

soup = BeautifulSoup (html,'html.parser')
soup = soup.get_text()

rg = re.compile('(?<=\d{2}\.\s).+?(?=\d{2}\.|$)')
trackList = rg.findall(soup)


newList =[]

for i in trackList:
     #replacing white space between words by '+' to create a proper google search URL
     newList.append(i.replace(" ","+"))
     

for i in newList:
    
    new = 2
    
    tabUrl = "http://google.com/#q=";
    
    term = i + "+zippyshare" #searching for matching zippyshare links
    
    webbrowser.open(tabUrl + term,new = new)
