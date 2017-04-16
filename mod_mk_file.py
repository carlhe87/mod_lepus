#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: 

This Module is used for creating n datafiles each contain data (default = None)
file location in PY_MOD sub-folder 
allow multi-level sub-folder from tuple
leaf folder name use text + serial number (ttlYYMMDD###) 

"""
import os
import sys
import pickle
import json
#import csv
from rabbit import PATH_PY
from rabbit import PATH_DATA
from mod_const import TMPL_PY_MOD

from mod_gen_serie import gen_serie


#major function
def make_file(name="temp", type="py", content=TMPL_PY_MOD, interlevel=("","temp")):
    """create empty file, auto rename upon name conflict, fill with py2 mod template"""
    #construct filename
    filename = ".".join((name,type))
    #build directory
    interpath = "/".join((interlevel))
    directory = "/".join((PATH_PY, interpath))
    path = "/".join((directory, filename))
     
    #If directory not exist, make directory recursively and create file
    if not os.path.exists(directory):
        os.makedirs(directory)
        with open(path,"a") as f: 
            f.write(content)
    else: pass
    # check existance and determine filename
    i = 1
    while os.path.exists(path):     
        filename = "{}_{}.{}".format(name, i, type)
        path = "/".join((directory, filename))
        i += 1
    # make file
    with open(path,"a") as f:
        f.write(content)
    # report
    if i > 1: 
        print "Name conflict, rename file as: {}".format(filename)
    else: 
        print "File created: {}".format(filename)
    print "directory: ", directory

def make_data(n=1, folder_text="data", content=None, interlevel=()):
    """create empty file, with serie number"""
    #generate folder name
    folder = gen_serie(folder_text, digit=4) #set serial# digit = 4
    #build directory
    interpath = "/".join((interlevel))
    directory = "/".join((PATH_DATA, interpath, folder))
    
    #If directory not exist, make directory recursively
    if not os.path.exists(directory):
       os.makedirs(directory)
    else: pass
    
    #generate file list
    file_reg = [] 
    for ref in range(n):    
        #save each instance of class to a file 
        with open(os.path.join(directory, str(ref)),"w+") as f:
            a = content                # create an instance            
            pickle.dump(a,f)            # save instacne to file
            file_reg.append([ref, str(f)])   # record file name and str address
    # save file_reg
    with open(os.path.join(directory,"file_list_info.txt"),"w+") as summary:
        json.dump(file_reg, summary)
    
    #report 
    print "Data files created, folder: {} count: {}".format(folder, n)
    print "directory: ", directory
    

def _main(*argv):
    make_file()
    #make_data(interlevel=argv[1:])
if __name__ == "__main__": 
    sys.exit(_main(*sys.argv))



