#imports all tkinter methods
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font

#GLOBAL VARIABLES 
tour = ""
duration = ""
reason = ""
number = ""
line = {"tour":tour,"duration":duration,"reason":reason,"number":number}
global counter
counter = 0

#window options
TourWin = Tk()
TourWin.title("Tour Number")
TourWin.resizable(width=False, height=False)

#Labels
TourLbl = Label(TourWin,text="Tour",font=("Helvetica", 16))
TourLbl.grid(row=0,column=0)
TourLbl.config(width=10)
TourLblFont = font.Font(TourLbl, TourLbl.cget("font"))
TourLblFont.configure(underline=True)
TourLbl.configure(font=TourLblFont)

ReasonLbl = Label(TourWin,text="Late Duration",font=("Helvetica", 16))
ReasonLbl.grid(row=0,column=1)
ReasonLbl.config(width=10)
ReasonLblFont = font.Font(ReasonLbl, ReasonLbl.cget("font"))
ReasonLblFont.configure(underline=True)
ReasonLbl.configure(font=ReasonLblFont)

TourLbl2 = Label(TourWin,text="Reason",font=("Helvetica", 16))
TourLbl2.grid(row=0,column=2)
TourLbl2.config(width=10)
TourLbl2Font = font.Font(TourLbl2, TourLbl2.cget("font"))
TourLbl2Font.configure(underline=True)
TourLbl2.configure(font=TourLbl2Font)

NumberLbl = Label(TourWin,text="Number",font=("Helvetica", 16))
NumberLbl.grid(row=0,column=3,columnspan=2)
NumberLbl.config(width=10)
NumberLblFont = font.Font(NumberLbl, NumberLbl.cget("font"))
NumberLblFont.configure(underline=True)
NumberLbl.configure(font=NumberLblFont,justify=RIGHT)


#Column 1 Objects
column_1_tours = ["Tour1 5:50","Tour2, 6:00","Tour3, 7:00"]
column_1_var = StringVar()

for val, tour in enumerate(column_1_tours):
    Radiobutton(TourWin,text=tour,indicatoron=0,width=10,padx=10,value=tour,variable=column_1_var).grid(row=val+1,column=0)

#Column 2 Objects
late_var = StringVar()
late_duration = Entry(TourWin,textvariable=late_var,width=10)
late_duration.grid(row=1,column=1)

#Column 3 Objects
column_3_reasons = ["verkehrsbedingt","Ausfall Kfz","zu spät vom BZ","zu spät vom PZ","sonstiges"]
column_3_var = StringVar()

for val, reason in enumerate(column_3_reasons):
    print(reason)
    Radiobutton(TourWin,text=reason,indicatoron=0,width=10,padx=10,value=reason,variable=column_3_var).grid(row=val+1,column=2)

#Column 4 Objects
Beh1Lbl = Label(TourWin,text="Beh 1 (SKBf)",justify=RIGHT)
Beh1Lbl.grid(row=1,column=3)
Beh1Lbl.config(width=10)
beh1_field = IntVar()
Beh1Entry = Entry(TourWin,textvariable=beh1_field,width=10)
Beh1Entry.grid(row=1,column=4)

Beh2Lbl = Label(TourWin,text="Beh 2 (GBf)",justify=RIGHT)
Beh2Lbl.grid(row=2,column=3)
Beh2Lbl.config(width=10)
beh2_field = IntVar()
Beh2Entry = Entry(TourWin,textvariable=beh2_field,width=10)
Beh2Entry.grid(row=2,column=4)

Beh3Lbl = Label(TourWin,text="Beh 3 (MBf)",justify=RIGHT)
Beh3Lbl.grid(row=3,column=3)
Beh3Lbl.config(width=10)
beh3_field = IntVar()
Beh3Entry = Entry(TourWin,textvariable=beh3_field,width=10)
Beh3Entry.grid(row=3,column=4)

Beh4Lbl = Label(TourWin,text="Rbeh",justify=RIGHT)
Beh4Lbl.grid(row=4,column=3)
Beh4Lbl.config(width=10)
beh4_field = IntVar()
Beh4Entry = Entry(TourWin,textvariable=beh4_field,width=10)
Beh4Entry.grid(row=4,column=4)


#Tree
tree = ttk.Treeview(TourWin, height=10,columns=('Late Duration','Reason','Number'),selectmode="extended")
tree.heading('#0', text="Tour",anchor=W)
tree.heading('#1', text="Late Duration",anchor=W)
tree.heading('#2', text="Reason",anchor=W)
tree.heading('#3', text="Number",anchor=W)
tree.column('#0',stretch=YES,width=50)
tree.column('#1',stretch=YES,width=50)
tree.column('#2',stretch=YES,width=50)
tree.column('#3',stretch=YES,width=50)
tree.grid(row=7,columnspan=5,sticky='nsew')
treeview=tree

#Buttons
AddBtn = Button(TourWin,text="Add",height=5,width=13,command=lambda:add())
AddBtn.grid(row=8,column=0)

ClearBtn = Button(TourWin,text="Clear",height=5,width=13,command=lambda:clearFields())
ClearBtn.grid(row=8,column=1)

MiscBtn = Button(TourWin,text="CheckStat..",height=5,width=13)
MiscBtn.grid(row=8,column=2)

Misc2Btn = Button(TourWin,text="Misc.",height=5,width=13)
Misc2Btn.grid(row=8,column=3)

ExitBtn = Button(TourWin,text="Exit",height=5,width=13,command=lambda:TourWin.destroy())
ExitBtn.grid(row=8,column=4)


def printStat(var):
    print("you have selected "+var.get())

def clearFields():
    #this functions recieves all checkboxes and text fields in the window and clears them
    Beh1Entry.delete(0,'end')
    Beh2Entry.delete(0,'end')
    Beh3Entry.delete(0,'end')
    Beh4Entry.delete(0,'end')
    late_duration.delete(0,'end')
    column_1_var.set("")
    column_3_var.set("")

def add():
    line["tour"] = column_1_var.get()
    line["duration"] = late_duration.get()
    line["reason"] = column_3_var.get()
    line["number"] = "testing"
    addedTour = line["tour"]
    addedDuration = line["duration"]
    addedReason = line["reason"]
    addedNumber = line["number"]
    tree.insert("",0,text=addedTour,values=(addedDuration,addedReason,addedNumber))



TourWin.mainloop()

