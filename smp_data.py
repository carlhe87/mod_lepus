"""sample data file 

	smp_pg_prop # sample page property data
	smp_menu # sample menu data
	
"""
# sample page property data
smp_pg_prop = {
	"ref":"page ref",
	"ID":"page ID",
	"name":"page name",
	"heading":"page heading",
	"info":"page info",
	"content":"page content",
	"menu":"page menu",
	"ending":"page ending",
	}

# sample menu data
smp_menu ={
	1 : "menu1",
	2 : "menu2",
	3 : "menu3", # number key as menu
	"mn_text" : "you have 3 options", #text for menu description
	"cmd_quest" : "continue?", #text for command request
	"Y": "Yes",
	"N": "NO",
	"dft_cmd": "Y",
	} 


# library

pg_rm_A = {
	"name":"room A",
	"ID": "pg_rm#1",
	"heading":"title A",
	"info": "here is room A",
	"ending": "page 1"
	}
pg_rm_B  = {
	"name":"room B",
	"ID": "pg_rm#2",
	"heading":"title B",
	"info": "here is room B",
	"ending": "page 2"
	}
pg_rm_C = {
	"name":"room C",
	"ID": "pg_rm#3",
	"heading":"Section 3",
	"info": "here is room C",
	"ending": "Page 3"
	}

menu_A = {
	1 : "Room A",
	2 : "Room B",
	3 : "Room C", 
	"mn_text" : "Where do you want to go?", #default text for menu description
	"cmd_quest" : "Exit game?", #default text for command request
	"Y": "Yes",
	"N": "NO",
	"dft_cmd": 1,
	}

menu_B = {
	1 : "Room A",
	2 : "Room B",
	3 : "Room C", 
	"mn_text" : "Where do you want to go?", #default text for menu description
	"cmd_quest" : "Exit game?", #default text for command request
	"Y": "Yes",
	"N": "NO",
	"dft_cmd": 2,
	}

menu_C = {
	1 : "Room A",
	2 : "Room B",
	3 : "Room C", 
	"mn_text" : "Where do you want to go?", #default text for menu description
	"cmd_quest" : "Exit game?", #default text for command request
	"Y": "Yes",
	"N": "NO",
	"dft_cmd": 3,
	} 

smp_content = "This is a very long article, let's say it is 200 pg long"

pg_lib =[
	(pg_rm_A, menu_A, smp_content),
	(pg_rm_B, menu_B, smp_content),
	(pg_rm_C, menu_C, smp_content),	
	]
	
# library of preset cmd for menu --> single str 
preset_cmd_lib = {
	"E":"Next",
	"B":"Back",
	"Y":"Yes",
	"N":"No",
	"O":"OK",
	"C":"Cancel",
	"X":"Exit",
	} 
# library of usrdef_text --> long str
usrdef_text_lib = {
	"mn_text" : "menu description", #default text for menu description
	"cmd_quest" : "next step?", #default text for command request
	} 
