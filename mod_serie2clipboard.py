#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: 

This Module is used for
"""
#innitial import
import sys #.path for setting env, .argv for taking parameter
import rabbit
from mod_gen_serie import gen_serie
from mod_clip_board import clip_board

def serie2clipboard():
    clip_board(gen_serie())
s2c = serie2clipboard
    
#main
def _main(*argv): 
    serie2clipboard()

if __name__ == "__main__": 
    sys.exit(_main(*sys.argv))
