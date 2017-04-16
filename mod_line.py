#-*- coding:utf-8 -*-
def line(style = None, tot_len = 50, info = ""):
	""" return a <str> line
	
		input:
			arg1 <int> predefined styles
			arg1 <str> single mark
			arg1 None default mark
			arg2 <int> total length
			arg3 <str> infomation
		
		default ----------
		can insert info	without affecting total length
			defact: each chinese char in info cause 1 unit additional length
				solution: detect chinese char and make correction
				comment: not urgent defact
	"""
	mark = "-" #default mark
	long_len = 65
	short_len = 35
	
	style_lib = {
		0:("=", long_len, ""),
		1:("*", long_len, "Start of page"),
		2:("*", long_len, "End of page"),
		3:("-", short_len, ""),
		4:("=", short_len, ""),
		5:("*", short_len, ""),
		} # require an <int> style index
	
	#screen for predefined styles
	if style == None:
		pass
	elif type(style) is int:
		if style in style_lib: #assume <int>
			mark, tot_len, info = style_lib[style]
		else: 
			print "Error: line() undefined style type"
	elif type(style) is str:
		if len(style) == 1: # define mark 
			mark = style	
		else: 
			print "Error: line() mark length too large"
	else:
		print "Error: Unexpected arg"
	
	if info != "":
		text = " " + info + " "
	else: 
		text = info
	
	half_len = (tot_len - len(text)-2)/2
	if half_len < 2: half_len = 2
	if (tot_len - len(text)) % 2 == 1:
		add_len = 1
	else: add_len = 0
	
	
	#general line form
	pipline = "\n" + mark * half_len + text + mark * (half_len + add_len) + "\n"
	
	#main 
	return pipline
	
