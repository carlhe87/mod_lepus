#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: time_stamp with GUI

This Module is update of mod_time_stamp. 
    allow online custom text addition
    
"""
import datetime
from Tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)
        self.a = IntVar()
        self.a.set(0)
        self.b = IntVar()
        self.b.set(8)
        self.txt = StringVar()
        self.txt.set("CWH#")
        self.stamp = StringVar()
        self.stamp.set("YYYYMMDD")
        self.final_stamp = StringVar()
        self.final_stamp.set("".join((self.txt.get(), self.stamp.get())))
        self.createWidgets()

    def createWidgets(self):        
        #frame_top1
        self.topframe1 = Frame(self,width=20)
        self.topframe1.pack(side="top", anchor="w", padx=5, pady=10)
        #label_txt
        self.ent_txt = Label(self.topframe1, text="initial text:", width=8)
        self.ent_txt.pack(side="left",anchor="w")
        #entry_txt
        self.ent_txt = Entry(self.topframe1, textvariable=self.txt, width=8)
        self.ent_txt.pack(side="top",anchor="e")
        self.ent_txt.bind('<Key-Return>', self.stamp_update)

        #frame_top2
        self.topframe2 = Frame(self,width=30)
        self.topframe2.pack(side="top", anchor="w", padx=5, pady=0)
        #label_begin
        self.ent_a = Label(self.topframe2, text="begin:", width=5)
        self.ent_a.pack(side="left",anchor="nw")
        self.ent_a = Entry(self.topframe2, textvariable=self.a, width=2)
        self.ent_a.pack(side="left",anchor ="ne")
        self.ent_a.bind('<Key-Return>', self.stamp_update)       
        #label_end
        self.ent_b = Label(self.topframe2, text="end:", width=5)
        self.ent_b.pack(side="left",anchor="sw")
        self.ent_b = Entry(self.topframe2, textvariable=self.b, width=2)
        self.ent_b.pack(side="left",anchor = "se")
        self.ent_b.bind('<Key-Return>', self.stamp_update)
        
        #copy to clipboard button
        self.c2cb = Button(self)
        self.c2cb["text"] = "copy to clipboard"
        self.c2cb["fg"]   = "black"
        self.c2cb["command"] = self.copy2cb
        self.c2cb.pack({"side": "bottom"})
        #quit button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "bottom"})
        #display final stamp
        self.topframe3 = Frame(self,width=20)
        self.topframe3.pack(side="top", anchor="ne", padx=5, pady=0)
        self.stamp_preview = Message(self.topframe3, textvariable=self.final_stamp)
        self.stamp_preview.pack(side="bottom", anchor="e")
            
    def copy2cb(self):
        self.stamp.set(time_stamp(self.a.get(), self.b.get()))
        self.final_stamp.set("".join((self.txt.get(), self.stamp.get())))
        copy2clipboard(self.final_stamp.get())
        
    def stamp_update(self, event):
        self.copy2cb()

        
def copy2clipboard(input="here is clipboard"):
    r = Tk() #start a new window
    r.withdraw() #hide window
    r.clipboard_clear()
    r.clipboard_append(input)
    #r.destroy() #this cause ERROR in other software! deactivate it 
    #
    result = r.selection_get(selection = "CLIPBOARD")
    print "now in clipboard:\n", result #debug

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
    output = []
    for i in range(begin, end):
        output.append(timestamp[i])
    return "".join(output)

def main():   
    root = Tk()
    root.title("time stamp v2.0")
    root.geometry("320x280")
    app = App(master=root)
    app.mainloop()
    root.destroy()

main()