#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: Rabbit Start!

This Module is used for creating a temp.py in current folder
    -append path of my_mods to sys.path
    -import CONST file path for template in mod_const
    -create a set of template py file if not exist

How to use:
    import this mod or run .pyc once
"""
import os

if "sys" not in dir():
    import sys   
    sys.path.append("C:/Users/Carl W He/Documents/Python/Scripts/mod/mod_lepus/")

from mod_const import TMPL_PY_CONST
from mod_const import TMPL_PY_MAIN
from mod_const import TMPL_PY_INIT

if not os.path.exists("const.py"):
    with open("const.py","w+") as f:
        f.write(TMPL_PY_CONST)
        print "const file generated"

if not os.path.exists("main.py"):
    with open("main.py","w+") as f:
        f.write(TMPL_PY_MAIN)
        print "main file generated"
        
if not os.path.exists("__init__.py"):
    with open("__init__.py","w+") as f:
        f.write(TMPL_PY_INIT)
        print "init file generated"
