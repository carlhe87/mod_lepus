from mod_input_mtd import input_int, input_menu_cmd #usr defined input
from mod_line import line # <str> line
from smp_data import pg_lib # sample data

class menu(object):
	"""generate menu and command list
		
		arg: <lib> 
				cmd<int> : menu<str>  --> extract usrdef_cmd
			+ 	title<str> : text<str> --> extract usrdef_text
			+	index<str> : text<str> --> extract preset_cmd 
		output:
			self.menu_str_gen() --> display content <str>
			self.menu_cmd_gen() --> cmd list <dict>
	"""
	preset_cmd_lib = {
		"E":"Next",
		"B":"Back",
		"Y":"Yes",
		"N":"No",
		"O":"OK",
		"C":"Cancel",
		"X":"Exit",
		} # preset-menu: cmd --> single str 
	usrdef_text_lib = {
		"mn_text" : "menu description", #default text for menu description
		"cmd_quest" : "next step?",
		"dft_cmd": None, #default text for command request
		} # usr-def cmd --> long str
		

	def __init__(self, new_menu = {}):
		
		self.usrdef_text = dict(menu.usrdef_text_lib) # default dict for usrdef_text
		self.preset_cmd = {} # empty dict for preset_cmd
		self.usrdef_cmd = {} # empty dict for usrdef_cmd
		self.other_cmd = {} # empty dict for other_cmd
		self.menu_cmd = {} #empty dict for all cmd
		self.dft_cmd = None #default cmd
		
		#sort cmd in new_menu into three sections
		for key in new_menu.keys(): 
			# usrdef_cmd
			if type(key) == int: 
				self.usrdef_cmd[key] = new_menu[key]
			# preset_cmd
			elif type(key) == str and key in menu.preset_cmd_lib:
				self.preset_cmd[key] = new_menu[key]
			# other_cmd
			elif type(key) == str and len(key) == 1:
				self.other_cmd[key] = new_menu[key]
			# usrdef_text
			elif type(key) == str:
				self.usrdef_text[key] = new_menu[key]
			else:
				print "Error: unexpected new_menu"
		
		#extract defaut cmd
		if "dft_cmd" in self.usrdef_text.keys():
			self.dft_cmd = self.usrdef_text["dft_cmd"]
			
	def menu_str_gen(self):
		mn_output = ""
		mn_output += line()

		#prompt menu description
		mn_output += self.usrdef_text["mn_text"]
		mn_output += "\n"
		#generate usrdef_cmd menu
		for key in self.usrdef_cmd.keys():
			mn_output += "{}. ".format(key)
			mn_output += self.usrdef_cmd[key]
			mn_output += "\n"
		
		mn_output += line()
		
		#prompt cmd_quest 
		mn_output += self.usrdef_text["cmd_quest"]
		mn_output += " " * 4
		#generate other_cmd menu
		for cmd in self.other_cmd.keys():
			mn_output += "{}. ".format(cmd)
			mn_output += self.other_cmd[cmd]
			mn_output += " " * 4
		#generate preset_cmd menu
		for cmd in self.preset_cmd.keys():
			mn_output += "{}. ".format(cmd)
			mn_output += menu.preset_cmd_lib[cmd]
			mn_output += " " * 4

		mn_output += "\n"
		return mn_output #output for print
		
	def menu_cmd_gen(self):
		#for key in self.preset_cmd.keys():
		self.menu_cmd.update(self.preset_cmd)
		self.menu_cmd.update(self.usrdef_cmd)
		self.menu_cmd.update(self.other_cmd)
		
		return self.menu_cmd
	

class page(object):
	pg_reg_tbl = [] #list for page reg
	pg_ref_itr= 0 #unique page ref generator
	index_pg_lib ={} #create a ID:index dictionary, update every new instance
	
	tmpl_prop = {
		"ref":"page ref", #store self.ref --> unique code in pg_reg_tbl
		"ID": "page ID", #page content specific
		"name":"page name", # for debug and navigation
		"heading":"page heading", #displayed name
		"info":"page info", #displayed page intro
		"content":"page main content", # need load from pg_lib
		"menu":"page menu", # need load from pg_lib
		"ending":"page ending", #displayed page ending
		}#template for page properties
	
	def __doc__(self):
		"""general page template
		"""
	
	def __init__(self, *arg):
		self.new_obj = True
		self.pg_lib_index = None # current page calling index : pg_lib[index]
		self.prop = dict(page.tmpl_prop) #innitialize properties
		self.menu_cmd = {} #accepted command list
		self.ref = 0 # easy access to self.prop["ref"]

	#page registration
	def pg_reg(self):
		if self.new_obj:
			self.ref = page.pg_ref_itr #unique page tracking number 
			self.prop["ref"] = self.ref
			page.pg_ref_itr += 1 #generate unique ref number for each new page instance 
			page.pg_reg_tbl.append([self.ref, self.prop["name"], self, self.prop["ID"],0]) 
		else: pass
		
	#page operations	
	def pg_continue(self):
		raw_input("\npress ENTER to continue")
	def pg_exit(self):
		raw_input("\npress ENTER to exit")
	def pg_clear(self, n = 30):
		print("\n" * n)
	def pg_close(self):
		# de-register page, del from pg_reg_tbl
		for i in range(len(page.pg_reg_tbl)):
			if page.pg_reg_tbl[i][0] == self.ref:
				del page.pg_reg_tbl[i]
	def pg_keep(self):
		# suspend page, keep in pg_reg_tbl, count visit 
		for i in range(len(page.pg_reg_tbl)):
			if page.pg_reg_tbl[i][0] == self.ref:
				page.pg_reg_tbl[i][4] += 1 # count visit
	def pg_new(self, index = 0, mode = "keep"):
		#close/keep current page
		if mode == "close":
			self.pg_close()
		else:
			self.pg_keep() #default
				
		# create new instance of page
		new_page = page() #creat new instance
		new_page.pg_lib_index = index #pass index to new object
		new_page.pg_main(*pg_lib[index]) # load via index i from pg_lib
				
		return new_page #just location
		
	def pg_jump(self, pg_ref = 0, mode = "keep"):
		#close/keep current page
		if mode == "close":
			self.pg_close()
		else:
			self.pg_keep() #default
		
		# not creat new instance of page, go to previous page		
		for i in range(len(page.pg_reg_tbl)):
			if page.pg_reg_tbl[i][0] == pg_ref: #find registered target via <page>.ref 
				tgt_ID = page.pg_reg_tbl[i][3] #find target page ID
				tgt_index = page.index_pg_lib[tgt_ID] #get page loading index
				
				self = page.pg_reg_tbl[i][2]  #point self location to target location
				self.pg_lib_index = tgt_index #pass index to new obj
				self.new_obj = False
				self.pg_main(*pg_lib[tgt_index]) # reload with target index
				return
		
		print "Error pg_jump() find no target"
		return
		
	def reload(self):
		self.pg_jump(self.ref, "keep")
	
	#page debug	
	def pg_test(self):
		for key in self.prop.keys():
			print(self.prop[key])
		print "#page count:", len(page.pg_reg_tbl)
		print "#pg_reg", page.pg_reg_tbl
	
	def dbg_inspect(self):
		print "#page count:", len(page.pg_reg_tbl)
		for elm in page.pg_reg_tbl:
			print elm
		
		print "\n<'ID':index>\n"
		for key in page.index_pg_lib.keys():
			print "{} : {}".format(key, page.index_pg_lib[key])
	
	
	#page update contents
	def pg_load(self, *arg):
		"""load contents to slots in a page
		
			load prop from pg_prop <dict>
			load menu from menu obj <str>
			load content from content <str>
		"""
		prop_data, menu_data, cont_data = arg #unpack
		
		#call a instance of menu
		pg_menu = menu(menu_data) #creat a instance of Menu
		menu_str = pg_menu.menu_str_gen() #generate output string of menu
		self.menu_cmd = pg_menu.menu_cmd_gen() #generate cmd list of menu
		self.dft_cmd = pg_menu.dft_cmd #pass default cmd from menu to page	
		
		#update properties to current page
		for key in prop_data.keys(): 
			self.prop[key] = prop_data[key]
		
		#update index:ID entry
		page.index_pg_lib.update({self.prop["ID"] : self.pg_lib_index})
		
		#update menu<str>
		self.prop["menu"] = menu_str
		#update content <str>
		self.prop["content"] = cont_data

	#page display
	def pg_display(self):
		self.pg_clear()
		print line("*", info=self.prop["heading"])
		print self.prop["info"]
		print line()
		print self.prop["content"]
		print self.prop["menu"]
		print line("*", info=self.prop["ending"])
	
	def pg_current_ID(self):
		# find current page, via ref. report ID 
		for i in range(len(page.pg_reg_tbl)):
			if page.pg_reg_tbl[i][0] == self.ref: #find current page in reg_tbl via ref
				current_pg_ID = page.pg_reg_tbl[i][3] #current page ID
				return current_pg_ID
		
		#if not found
		print "page not found, page ref:", self.ref
		return None
	
	def pg_cmd(self):
		""" get command for next step
		
			cmd pass to page instance var
		"""
		input = None
		default = self.dft_cmd
		prompt = "please enter your command here:"
		while input == None: #final input value can not be None even if default = None 
			input = input_menu_cmd(prompt, default, self.menu_cmd)		
		return input

	def pg_action(self):
		"""context independent action 
			
			enter numbered room
		"""
		input = self.pg_cmd() # input can be <str> or <int>
		if input == "Y":
			return None
		elif input == "N":
			self.reload() # jump to current page via self.ref
		elif input in range (1,4):
			index = input - 1
			#mode 1: close page and new page, always new
			#self.pg_new(index, "close")
			#mode 2: keep page and jump to opened page, creat new only 1st time
			
			# check if page index known
			for tgt_ID in page.index_pg_lib.keys(): 
				if page.index_pg_lib[tgt_ID] == index: 
					if tgt_ID == self.pg_current_ID(): # if target is current page
						self.reload() #reload
						return
					else: #target is other opened page  
						for i in range(len(page.pg_reg_tbl)): 
							# page with given page ID is currently open 
							if page.pg_reg_tbl[i][3] == tgt_ID:
								pg_ref = page.pg_reg_tbl[i][0] # get current open page 
								self.pg_jump(pg_ref, "keep")
								return
						# page of tgt_ID not found in reg_tbl: once opened but now closed
						print "opened once but now closed"
						self.pg_new(index, "keep") #open a new page with index
						return
			# page index unknown
			print "index not found, create new" #debug
			self.pg_new(index, "keep")
			return
			
	def pg_main(self, *arg):
		"""main page
		"""
		self.pg_load(*arg)
		self.pg_reg()
		self.pg_display()
		self.pg_action()
		return None

"""
#main
page().pg_new(1)
page().pg_exit()
"""