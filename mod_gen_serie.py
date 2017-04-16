#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: 

This Module is used for
"""

import sys
import os
from mod_time_stamp import time_stamp
from mod_const import PATH_MOD

def reset_serie():
    path = "/".join((PATH_MOD,"mod_gen_serie.txt"))
    with open(path, "w") as f: f.truncate(0)
    print "serie reset!"
    
def gen_serie(text="", digit=2):
    """generate serie number
    
        format YYYYMMDD#### (e.g. 4-digit code)
        if number digit exceed 9999, 
            ### display start from 0000, 
            real number in mod_gen_serie.txt
            
        actual capability of coding 
    """    
    path = "/".join((PATH_MOD,"mod_gen_serie.txt"))
    #if file does not exist
    if not os.path.exists(path):
        with open(path, "w") as f: pass
    
    with open(path,"r+") as f:
        code = 1
        code_dsp=""
        #read content
        line1 = f.readline()[:-1]
        line2 = f.readline()
        #print "time stamp = ", line1
        #print "code = ", line2
        
        #check and modify content        
        stamp = time_stamp()[2:8] #use YYMMDD as time stamp
        if line1 != stamp or line2 is None:
            f.truncate(0)       #if not today, not yet number, or file empty
            code = 1 #rather than "01"
            code_dsp = "01" 
        else:
            code = int(line2) + 1
            if digit==2:
                code_dsp = "{:0>2}".format(code) #here digit set as 3
            elif digit==3:
                code_dsp = "{:0>3}".format(code) #here digit set as 4
            elif digit==4:
                code_dsp = "{:0>4}".format(code) #here digit set as 2
            else:
                code_dsp = "{:0>6}".format(code) #here digit set as 6
        serie = "".join((text, stamp, code_dsp))
        f.seek(0)
        f.writelines((stamp,"\n", str(code)))
        return  serie
        
#main
def _main(*argv):
    #reset_serie()
    gen_serie(*argv[1:])
if __name__ == "__main__": 
    sys.exit(_main(*sys.argv))
