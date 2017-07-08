#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 19:38:06 2017

@author: yannickleroux
"""

import webbrowser

term_list = "01. Coyote - Eve (The Kenneth Bager Experience Remix), \
02. Death On The Balcony - Addict For Your Love, \
03. Caribou - Your Love Will Set You Free (C2's Set U Free Remix), \
04. Rene Bourgeois - Soul Paradise (Sascha Braemer's Deep Sunrise Remix), \
05. Purple Disco Machine - Musique,\
06. Pete Tong feat. S.Y.F. - Dawn (Franky Rizardo Remix),\
07. DJ-Chart - Deep House Love,\
08. Luca Guerrieri - Harmony,\
09. Harry Romero & Joeski feat. Shawnee Taylor - Get It Right (Club Mix),\
10. Mike Mago - The Gift (Mark Knight Remix),\
11. Weiss - Our Love,\
12. Joey Negro feat. Alex Mills - Everybody Wants Something (Akabu Warehouse Mix),\
13. Franky Rizardo - Real Love,\
14. Audion feat. Troels Abrahamsen - Dem Howl (Joris Voorn Mix),"

trackList = term_list.split(',')
newList =[]

for i in trackList:
     newList.append(i.replace(" ","+"))
     

print (newList)

for i in newList:
    
    new = 2
    
    tabUrl = "http://google.com/#q=";
    
    term = i + "+zippyshare"
    
    webbrowser.open(tabUrl + term,new = new)
