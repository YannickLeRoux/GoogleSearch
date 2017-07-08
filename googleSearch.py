#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 19:38:06 2017

@author: yannickleroux
"""

import webbrowser

#J ai besoin d ajouter \ manuellemt so far, trouver une solution
#reprendre au podcast 30

term_list = ""


cleaned_term_list = term_list.translate ({ord(c): "+" for c in "!@#ü$%^&*()[]{};:,/<>?\|`~-=_+1234567890é"})


trackList = cleaned_term_list.split('.')
newList =[]

for i in trackList:
     newList.append(i.replace(" ","+"))
     

print (newList)

for i in newList:
    
    new = 2
    
    tabUrl = "http://google.com/#q=";
    
    term = i + "+zippyshare"
    
    webbrowser.open(tabUrl + term,new = new)
