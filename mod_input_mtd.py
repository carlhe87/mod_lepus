#-*- coding:utf-8 -*-

"""usr_defined input methods"""

def input_int(prompt = "request <int>", default = None):
	""" error proof input with default
	
	arg: 
		arg1 <str> prompt info
		arg2 <int> default value 
	output:
		normal: <int> accepted value 
		except: <int> default value
	"""
	output = prompt + " (default {})".format(default)
	
	try:	
		trial = int(raw_input(output))
		return trial
	except ValueError:
		print ("not a int, take default value")
		return default

def input_float(prompt = "request <float>", default = None):
	""" error proof input with default
	
	arg: 
		arg1 <str> prompt info
		arg2 <float> default value 
	output:
		normal: <float> accepted value 
		except: <float> default value
	"""
	output = prompt + " (default {})".format(default)
	
	try:	
		trial = float(raw_input(output))
		return trial
	except ValueError:
		print ("not a float, take default value")
		return default

def input_str(prompt = "request <str>", default = None):
	""" error proof input with default
	
	arg: 
		arg1 <str> prompt info
		arg2 <str> default value 
	output:
		normal: <str> accepted value 
		except: <str> default value
	"""
	output = prompt + " (default {})".format(default)
	
	try:	
		trial = raw_input(output)
		return trial
	except ValueError:
		print ("invalid string, take default value")
		return default
		
def input_menu_cmd(prompt = "request single <str>", default = None, cmd_dict = {}):
	""" error proof menu cmd input with default
	
	arg: 
		arg1 <str> prompt info
		arg2 <int> default cmd 
		arg3 <dict> valid cmd
	output:
		normal: <str> or <int> accepted value 
		except: <str> default value
	"""
	output = prompt + " (default {})".format(default)
	input = raw_input(output)
	
	try:
		trial = int(input)
		if trial in cmd_dict.keys():
			return trial # valid <int> cmd
	except ValueError:
		if input in cmd_dict.keys():
			return input # valid <str> cmd
	
	print ("invalid command, take default value")
	return default # invalid cmd

def input_seq(mode="int", prompt="please enter a sequence", splitter=",", default=None):
    """
    read user input string and split to a list, convert to integer or float if possible
    
    mode:
        "int": convert to <int> if possible (default)
        "float": covert to <float> if possible, not <int>
        "string": do not convert
    """
    text = "{} splitted by '{}', (default {})\n".format(prompt, splitter, default)
    
    def str2num(input, str2int=True):
        """
        try to convert <str> to <int>, otherwise <float>. otherwise give up        
        mode: "int","float"
        
        """
        try:
            temp = float(input)
            if not str2int:
                return temp             
            elif temp.is_integer():
                return int(temp)
            else:
                return temp 
        except ValueError:
            return input
            
    if mode == "int" or mode == "float":
        if mode == "int":
            str2int = True
        else: 
            str2int = False
        return [str2num(x, str2int) for x in raw_input(text).split(splitter)]
    elif mode == "string":
        return raw_input(text).split(splitter)
    else:
        print "Error: unexpected mode"
