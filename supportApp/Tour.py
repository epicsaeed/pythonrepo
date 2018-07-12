#imports tkinter methods
from tkinter import messagebox, Label, Button,font,Tk,Radiobutton,RIGHT,IntVar,StringVar,Entry,ttk,YES,W
import sqlite3
from datetime import datetime

conn = sqlite3.connect('tour.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS data(tour TEXT, duration TEXT, reason TEXT, number TEXT, date TEXT)''')
conn.commit()

#GLOBAL VARIABLES 
tour = ""
duration = ""
reason = ""
number = ""
date = ""
line = {"tour":tour,"duration":duration,"reason":reason,"number":number, "date":date}
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
    Radiobutton(TourWin,text=reason,indicatoron=0,width=10,padx=10,value=reason,variable=column_3_var).grid(row=val+1,column=2)

column_5_text = ["Beh 1 (SKBf)","Beh 2 (GBf)","Beh 3 (MBf)","Rbeh"]

#Column 4 Objects
Beh1Lbl = Label(TourWin,text=column_5_text[0],justify=RIGHT)
Beh1Lbl.grid(row=1,column=3)
Beh1Lbl.config(width=10)
beh1_field = StringVar()
Beh1Entry = Entry(TourWin,textvariable=beh1_field,width=10)
Beh1Entry.grid(row=1,column=4)

Beh2Lbl = Label(TourWin,text=column_5_text[1],justify=RIGHT)
Beh2Lbl.grid(row=2,column=3)
Beh2Lbl.config(width=10)
beh2_field = StringVar()
Beh2Entry = Entry(TourWin,textvariable=beh2_field,width=10)
Beh2Entry.grid(row=2,column=4)

Beh3Lbl = Label(TourWin,text=column_5_text[2],justify=RIGHT)
Beh3Lbl.grid(row=3,column=3)
Beh3Lbl.config(width=10)
beh3_field = StringVar()
Beh3Entry = Entry(TourWin,textvariable=beh3_field,width=10)
Beh3Entry.grid(row=3,column=4)

Beh4Lbl = Label(TourWin,text=column_5_text[3],justify=RIGHT)
Beh4Lbl.grid(row=4,column=3)
Beh4Lbl.config(width=10)
beh4_field = StringVar()
Beh4Entry = Entry(TourWin,textvariable=beh4_field,width=10)
Beh4Entry.grid(row=4,column=4)

#Tree
tree = ttk.Treeview(TourWin, height=10,columns=('Late Duration','Reason','Number','Date'),selectmode="extended")
tree.heading('#0', text="Tour",anchor=W)
tree.heading('#1', text="Late Duration",anchor=W)
tree.heading('#2', text="Reason",anchor=W)
tree.heading('#3', text="Number",anchor=W)
tree.heading('#4', text="Date",anchor=W)
tree.column('#0',stretch=YES,width=15)
tree.column('#1',stretch=YES,width=10)
tree.column('#2',stretch=YES,width=50)
tree.column('#3',stretch=YES,width=50)
tree.column('#4',stretch=YES,width=50)
tree.grid(row=7,columnspan=5,sticky='nsew')
treeview=tree

#Buttons
AddBtn = Button(TourWin,text="Add",height=5,width=13,command=lambda:add())
AddBtn.grid(row=8,column=0)

ClearBtn = Button(TourWin,text="Clear",height=5,width=13,command=lambda:clearFields())
ClearBtn.grid(row=8,column=1)

LoadBtn = Button(TourWin,text="Load",height=5,width=13,command=lambda:load())
LoadBtn.grid(row=8,column=2)

Misc2Btn = Button(TourWin,text="Misc.",height=5,width=13)
Misc2Btn.grid(row=8,column=3)

ExitBtn = Button(TourWin,text="Exit",height=5,width=13,command=lambda:TourWin.destroy())
ExitBtn.grid(row=8,column=4)

############################################ HELPER FUNCTIONS ############################################

def clearFields():
    #this functions recieves all checkboxes and text fields in the window and clears them
    beh1_field.set("")
    beh2_field.set("")
    beh3_field.set("")
    beh4_field.set("")
    late_var.set("")
    column_1_var.set("")
    column_3_var.set("")

def add():
    # print(checkDurationField()," , ",checkAllNumbersField()," , ",checkRadiobtns())
    # print("beh 1,",checkIndivisualField(beh1_field))
    # print("beh 2,",checkIndivisualField(beh2_field))
    # print("beh 3,",checkIndivisualField(beh3_field))
    # print("beh 4,",checkIndivisualField(beh4_field))
    if checkDurationField():
        if checkAllNumbersField() and checkIndivisualField(beh1_field) and checkIndivisualField(beh2_field) and checkIndivisualField(beh3_field) and checkIndivisualField(beh4_field):
            if checkRadiobtns():
                found = getNumberFields()
                line["tour"] = column_1_var.get()
                line["duration"] = late_duration.get()
                line["reason"] = column_3_var.get()
                line["number"] = found
                addedTour = line["tour"]
                addedDuration = line["duration"]
                addedReason = line["reason"]
                addedNumber = line["number"]
                addedTime = time()
                cur.execute('''INSERT INTO data (tour,duration,reason,number,date) VALUES(?,?,?,?,?)''',(addedTour,addedDuration,addedReason,addedNumber,addedTime))
                # conn.commit()
                tree.insert("",0,text=addedTour,values=(addedDuration,addedReason,addedNumber,addedTime))
            else:
                messagebox.showerror("Error","Please select atleast one button from each column")
        else:
            messagebox.showerror("Error","All Number fields are empty.")
    else:
        messagebox.showerror("Error","Please insert valid duration value. (00:00)")

def getNumberFields():
    allfields = [beh1_field.get(),beh2_field.get(),beh3_field.get(),beh4_field.get()]
    found = ""
    for i in range(4):
        print(allfields[i].isdigit())
        if allfields[i] != "" and allfields[i].isdigit():
            found+=column_5_text[i]+"="+str(allfields[i])+", "
        else:
            continue
    return found[:-2]
    
def view():
    conn.row_factory = dict_factory
    view = cur.execute('SELECT * FROM data').fetchall()
    print(view)

def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def load():
    conn.row_factory = dict_factory
    elements = cur.execute('SELECT * FROM data')
    for row in elements:
        tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
    messagebox.showinfo("Information","Database has been imported.")

def time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

############################################### ERROR CHECKING FUNCTIONS ###############################################
def checkDurationField():
    #checks if duration field of the format 00:00.
    time = str(late_var.get())
    if len(time) == 5:
        try:
            if (time[0:2]+time[3:5]).isdigit() and time[2] == ':':
                return True
        except AttributeError:
            return False
    return False

def checkIndivisualField(entry):
    return entry.get().isdigit()



def checkAllNumbersField():
    if beh1_field.get() == "" and beh2_field.get() == "" and beh3_field.get() == "" and beh4_field.get() == "":
        return False
    return True

def checkRadiobtns():
    if str(column_1_var.get()) != "" and str(column_3_var.get()) != "":
        return True
    return False

TourWin.mainloop()
