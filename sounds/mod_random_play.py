#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: play random wav file

This Module is used for sound notification
"""
import sys
import os
import random
import winsound
from pygame import mixer #allow play mp3


def play_sound(sound = "\a"):
    sound = choose_sound()
    if sound.endswith(".wav"):
        winsound.PlaySound(sound, winsound.SND_FILENAME)
    elif sound == "\a":
        print sound
    else: pass

def choose_sound():

    return pick
    

def _main(*argv):
    pass

if __name__ == "__main__": 
    _main(*sys.argv)
