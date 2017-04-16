#! /usr/bin/python
# -*- coding: utf-8 -*-

# version 1.2
"""Module Intro: Rabbit Start!

This Module is used for setting up env at local path
    -append ~/mod_lepus to sys.path
    -define CONST (file path) 
        ritual: direcotry end without /
        any new subfolder add / and end without /
    -load core rabbit mods for interactive mode
    
    NOTE: only for interactive mode! DO NOT import in scripts!

How to use:
    this mod is in C:\Python27\Lib\ (included in PYTHONPATH)
    to import all needed names, in cmd enter: from rabbit import *
"""
#innitial import
import sys  # .path for setting env, .argv for taking parameter
import os   # for file operation
sys.path.append("C:/Users/Carl W He/Documents/Python/Scripts/mod/mod_lepus")

#envrionment
PATH_PY = "C:/Users/Carl W He/Documents/Python/Scripts" 
PATH_DATA = "/".join((PATH_PY, "data"))
PATH_MOD = "/".join((PATH_PY, "mod/mod_lepus")) 
PATH_LEARN = "/".join((PATH_PY, "learn")) 

#primary import 
import mod_input_mtd

#secondary import
from mod_debug_tool import dsp_block_data as dsp
from mod_debug_tool import name_conflict as nc

def _new_proj():
    print "\nNext, you can create new mod or new proj by entering 'new'"
    if raw_input("\npress ENTER to skip, keywords to create new proj\n") == "new":
        import new_proj
        import new_mod
    else: pass

def _main(*argv):
    argv_slot = argv[:]
    
    #check
    if (sys.path[-1]) == PATH_MOD:
        print "\nInnitialization Successful! Do you wish to confirm?"
    else: print "sys.path setting Error!"
    #report
    if not raw_input("\npress ENTER to confirm, any other key to skip\n"):
        print "Last PYTHONPATH element:", (sys.path[-1])
    else: print "rabbit complete!"
    #create new proj
    _new_proj()

if __name__ == "__main__": #if run mod as script, show info, otherwise import quitely
    sys.exit(_main(*sys.argv))