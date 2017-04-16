#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: 

This Module is used for
"""
import sys
from Tkinter import Tk

def clip_board(input="here is clipboard"):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(input)
    result = r.selection_get(selection = "CLIPBOARD")
    #r.destroy() #this line cause ERROR! deactivate it 
    print "now in clipboard:\n", result

#main
def _main(*argv):
    clip_board(*argv)

if __name__ == "__main__": 
    sys.exit(_main(*sys.argv[1:]))
