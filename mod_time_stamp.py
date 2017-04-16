#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: 

This Module is used for
"""
import sys
import os
import datetime


def time_stamp(begin=0, end=8):
    """produce string of time stamp
    
        format
        "YYYYMMDDHHMMSS"
        "01234567890123"
        
        can adjust accuracy
        20170210 -->[0,8]
        170210 -->[2,8]
        17021022 -->[2,10]
    """
    
    now = datetime.datetime.now()
    t = now.timetuple()[:7]
    timestamp = "{:0>4}{:0>2}{:0>2}{:0>2}{:0>2}{:0>2}".format(t[0],t[1],t[2],t[3],t[4],t[5])
    return timestamp
    

def _main(*argv):
    print time_stamp(*argv)
if __name__ == "__main__": 
    sys.exit(_main(*sys.argv))
