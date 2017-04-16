#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: serie generator

This Module is used for generating serie number
if need digit modification, change in line 64
if need text modification, change in line 36
manually add text: use text.txt
"""
#constant
PATH_MOD = "C:/Users/Carl W He/Documents/Python/Scripts/mod/mod_lepus" 

from os.path import exists
from Tkinter import Tk
from datetime import datetime

def time_stamp(begin=0, end=8):
    """produce string of time stamp
    
        "YYYYMMDDHHMMSS"
        "01234567890123"    
        user can costom by slice: e.g. 170210 -->[2,8]
    """ 
    now = datetime.now()
    t = now.timetuple()[:7]
    timestamp = "{:0>4}{:0>2}{:0>2}{:0>2}{:0>2}{:0>2}".format(
                    t[0],t[1],t[2],t[3],t[4],t[5])
    return timestamp

def clip_board(input=""):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(input)
    result = r.selection_get(selection = "CLIPBOARD")

def gen_serie(text="lit"):
    """generate serie number
    
        format textYYMMDD##
        if number digit exceed 99, 
            ## display start from 00, 
            real number in local file serie.txt
            
        actual capability of coding 
    """         
    with open("serie.txt","r+") as f:
        code = 1
        code_dsp=""
        #read content
        line1 = f.readline()[:-1] #read 1st line, swallow "\n"
        line2 = f.readline()[:-1] #read 2nd line, swallow "\n"
        text = f.readline() #read 3rd line,
        #check and modify content        
        stamp = time_stamp()[0:8] #trim YYMMDD as time stamp
        if line1 != stamp:
            #if not today, or file empty, reset code
            code = 1 #rather than "01"
            code_dsp = "01" 
        else:
            code = int(line2) + 1
            code_dsp = "{:0>2}".format(code) #here digit set as 2
           
        serie = "".join((text, stamp, code_dsp))
        f.seek(0)
        f.writelines((stamp,"\n", str(code),"\n"))
        return  serie

#main
#if file does not exist create file locally
if not exists("serie.txt"):
    with open("serie.txt", "w") as f: pass
clip_board(gen_serie())
print "\a"