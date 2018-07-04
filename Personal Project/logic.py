#imports all tkinter methods
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font


def TourNumber():

    #window options
    TourWin = Tk()
    TourWin.title("Tour Number")
    # TourWin.geometry("300x200+300+300")
    TourWin.resizable(width=False, height=False)

    #Labels
    TourLbl = Label(TourWin,text="Tour",font=("Helvetica", 16))
    # TourLbl.pack(side=TOP,padx=5,pady=5)
    TourLbl.grid(row=0,column=0)
    TourLbl.config(width=10)
    TourLblFont = font.Font(TourLbl, TourLbl.cget("font"))
    TourLblFont.configure(underline=True)
    TourLbl.configure(font=TourLblFont)

    ReasonLbl = Label(TourWin,text="Reason",font=("Helvetica", 16))
    ReasonLbl.grid(row=0,column=1)
    ReasonLbl.config(width=10)
    ReasonLblFont = font.Font(ReasonLbl, ReasonLbl.cget("font"))
    ReasonLblFont.configure(underline=True)
    ReasonLbl.configure(font=ReasonLblFont)

    NumberLbl = Label(TourWin,text="Number",font=("Helvetica", 16))
    NumberLbl.grid(row=0,column=2,columnspan=2)
    NumberLbl.config(width=10)
    NumberLblFont = font.Font(NumberLbl, NumberLbl.cget("font"))
    NumberLblFont.configure(underline=True)
    NumberLbl.configure(font=NumberLblFont,justify=RIGHT)

    # Column 1 Objects
    checkBox1 = IntVar()
    cb1_text = "Tour1, 5:50"
    tour1_cb = Checkbutton(TourWin, text=cb1_text, variable = checkBox1).grid(row=1,column=0)
    # tour1_cb = Checkbutton(TourWin, text=cb1_text, variable = checkBox1).grid(row=1,column=0)

    checkBox2 = IntVar()
    cb2_text = "Tour2, 6:00"
    tour2_cb = Checkbutton(TourWin, text=cb2_text, variable = checkBox2).grid(row=2,column=0)
    # tour2_cb = Checkbutton(TourWin, text=cb2_text, variable = checkBox2).grid(row=2,column=0)

    checkBox3 = IntVar()
    cb3_text = "Tour3, 7:00"
    tour3_cb = Checkbutton(TourWin, text=cb3_text, variable = checkBox3).grid(row=3,column=0)
    # tour3_cb = Checkbutton(TourWin, text=cb3_text, variable = checkBox3).grid(row=3,column=0)

    #Column 2 Objects
    checkBox4 = IntVar()
    cb4_text = "verkehrsbedingt"
    checkbtn4 = Checkbutton(TourWin, text=cb4_text, variable = checkBox4,justify=LEFT).grid(row=1,column=1)
    #  checkbtn4 = Checkbutton(TourWin, text=cb4_text, variable = checkBox4,state=DISABLED,justify=LEFT).grid(row=1,column=1)

    checkBox5 = IntVar()
    cb5_text = "Ausfall Kfz"
    checkbtn5 = Checkbutton(TourWin, text=cb5_text, variable = checkBox5,justify=LEFT).grid(row=2,column=1)

    checkBox6 = IntVar()
    cb6_text = "zu spät vom BZ"
    checkbtn6 = Checkbutton(TourWin, text=cb6_text, variable = checkBox6,justify=LEFT).grid(row=3,column=1)

    checkBox7 = IntVar()
    cb7_text = "zu spät vom PZ"
    checkbtn7 = Checkbutton(TourWin, text=cb7_text, variable = checkBox7,justify=LEFT).grid(row=4,column=1)

    checkBox8 = IntVar()
    cb8_text = "sonstiges"
    checkbtn8 = Checkbutton(TourWin, text=cb8_text, variable = checkBox8,justify=LEFT).grid(row=5,column=1)

    #Column 3 Objects

    Beh1Lbl = Label(TourWin,text="Beh 1 (SKBf)",justify=RIGHT)
    Beh1Lbl.grid(row=1,column=2)
    Beh1Lbl.config(width=10)
    beh1_field = IntVar()
    Beh1Entry = Entry(TourWin,textvariable=beh1_field,width=10)
    # Beh1Entry.configure(state="disabled")
    Beh1Entry.grid(row=1,column=3)

    Beh2Lbl = Label(TourWin,text="Beh 2 (GBf)",justify=RIGHT)
    Beh2Lbl.grid(row=2,column=2)
    Beh2Lbl.config(width=10)
    beh2_field = IntVar()
    Beh2Entry = Entry(TourWin,textvariable=beh2_field,width=10)
    # Beh2Entry.configure(state="disabled")
    Beh2Entry.grid(row=2,column=3)

    Beh3Lbl = Label(TourWin,text="Beh 3 (MBf)",justify=RIGHT)
    Beh3Lbl.grid(row=3,column=2)
    Beh3Lbl.config(width=10)
    beh3_field = IntVar()
    Beh3Entry = Entry(TourWin,textvariable=beh3_field,width=10)
    # Beh3Entry.configure(state="disabled")
    Beh3Entry.grid(row=3,column=3)

    Beh4Lbl = Label(TourWin,text="Rbeh",justify=RIGHT)
    Beh4Lbl.grid(row=4,column=2)
    Beh4Lbl.config(width=10)
    beh4_field = IntVar()
    Beh4Entry = Entry(TourWin,textvariable=beh4_field,width=10)
    # Beh4Entry.configure(state="disabled")
    Beh4Entry.grid(row=4,column=3)

    #Column 4 objects

    #Buttons
    AddBtn = Button(TourWin,text="Add",width=10,height=2)
    AddBtn.grid(row=1,column=5)

    ClearBtn = Button(TourWin,text="Clear fields",width=10,height=2)
    ClearBtn.grid(row=2,column=5)

    ExitBtn = Button(TourWin,text="Save and Exit",width=10,height=2)
    #ExitBtn.grid(row=3,column=5)

    #Tree
    tree = ttk.Treeview(TourWin)
    tree["columns"] = ("one","two","three","four")
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.column("three", width=100)
    tree.column("four", width=100)
    tree.heading("one", text="No.")
    tree.heading("two", text="Tour")
    tree.heading("three", text="Reason")
    tree.heading("four", text="Number")
    tree.grid(row=7,columnspan=4)
    tree.insert("", 0, text="Details of added items:", values=("1","Tour 2","Ausfall Kfz","Rbeh 12:44"))

    TourWin.mainloop()