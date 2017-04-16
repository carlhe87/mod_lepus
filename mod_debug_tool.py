#! /usr/bin/python
# -*- coding: utf-8 -*-

"""rabbit debug tools

    This Module is used for debug in command line interface(CLI)
"""

# display block data in a indexed table
def dsp_block_data(target, name = "NA"):
    """\
        transform long wrapping list to a two-column table with index
    
        input target can be any type
    """
    typ = type(target)
    
    print "\n"*3,"="*9,"dsp() begin","="*9
    print "\n","{:>5} : {}\n{:>5} : {}".format("name", name, "type",typ)
    try:
        print "{:>5} : {}".format("count",len(target))
    except:
        print "Error: wrong type for dsp()\nname: {1}\ntype: {0}".format(typ, name)
        return None
        
    if typ == dict:
        print "\n  <key>  --> <value>\n","-"*20
        for key in target.keys():
            print "{0:>8} --> {1}".format(key, target[key])
    else:
        try:
            print "\n <index> --> <content>\n","-"*20
            for i in range(len(target)):
                print "{0:>8} --> {1}".format(i, target[i])
        except:
            print "unexpected target type:", type(target)
            return
    print "\n","="*10,"dsp() end","="*10
    
dsp = dsp_block_data

#check variable name conflict with built-in names
def name_conflict(name1=dir(), name2=dir(__builtins__),mod=None):
    """check local name conflict with sys built-in names
    
        input1: <list> name set, default local dir()
        input2: <list> name set, default local dir()
        input3: <module>, default no mod 
        
        
        usage:
        put following line at the END(after all vars) of the target code block 
        and enter following line under interactive mode
        from rabbit import nc; nc(dir(),dir(__builtins__))
    """
    name1 = set(name1) - {'__doc__', '__name__', '__package__'}
    name2 = set(name2)
    if mod is not None:
        mod_builtin = set(dir(mod.__builtins__))
        name2 = name2 | mod_builtin
    overlap = sorted(list(name1.intersection(name2)))
    return overlap