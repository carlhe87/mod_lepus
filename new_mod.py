#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: Rabbit Start!

This Module is used for creating a temp.py in the working directory
    -append path of my_mods to sys.path
    -import CONST file path for template in mod_const
    -create a template mod py file if not exist

How to use:
    import this mod or run .pyc once
"""
import os

if "sys" not in dir():
    import sys   
    sys.path.append("C:/Users/Carl W He/Documents/Python/Scripts/mod/mod_lepus/")

from mod_const import TMPL_PY_MOD

if not os.path.exists("tmp_mod.py"):
    with open("tmp_mod.py","w+") as f:
        f.write(TMPL_PY_MOD)
        print "Files generated"

