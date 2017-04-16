#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: CONST library

This Module is a storage of constants and tempaltes
can be called by mods used in my_mod

"""

# Begin
# Path
PATH_PY = "C:/Users/Carl W He/Documents/Python/Scripts" 
PATH_DATA = "/".join((PATH_PY, "data"))
PATH_MOD = "/".join((PATH_PY, "mod/mod_lepus")) 
PATH_LEARN = "/".join((PATH_PY, "learn")) 

# Empty file template
#for .py modules
TMPL_PY_MOD = """\
#! /usr/bin/python
# -*- coding: utf-8 -*-

\"""Module Intro: 

This Module is used for
\"""
import sys
import os
import json
import pickle

#main
def _main(*argv): pass

if __name__ == "__main__": 
    sys.exit(_main(*sys.argv))
"""

TMPL_PY_CONST = """\
#! /usr/bin/python
# -*- coding: utf-8 -*-

\"""Module Intro: CONST lib of current proj

This Module is used for storage of package consts
\"""

#main
"""

TMPL_PY_INIT = """\
#! /usr/bin/python
# -*- coding: utf-8 -*-

\"""Module Intro: __init__ of current package

This Module is used for initiation of package
\"""

#main
"""

TMPL_PY_MAIN = """\
#! /usr/bin/python
# -*- coding: utf-8 -*-

\"""Module Intro: main mod of current package

This Module is used as main file for  package
\"""

#main
def _main(*argv): pass

if __name__ == "__main__": 
    sys.exit(_main(*sys.argv))
"""