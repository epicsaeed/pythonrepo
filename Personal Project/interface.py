#imports all tkinter methods
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import logic

#creates window object
window = Tk()
window.title("SUPPORT APPLICATION")
window.resizable(width=False, height=False)

#Initiates main buttons
TourBtn = Button(window, text="Tour",width=20,height=5,command=lambda:logic.TourWindow())
TourBtn.grid(row=0,column=0)

WrongDepotBtn = Button(window, text="Fehlerhafte Zuführung",width=20,height=5)
WrongDepotBtn.grid(row=0,column=1)

LeftoverBtn = Button(window, text="Rückstände im ZSP",width=20,height=5)
LeftoverBtn.grid(row=1,column=0)

InfoBtn = Button(window, text="sonstige Informationen",width=20,height=5)
InfoBtn.grid(row=1,column=1)

StartBtn = Button(window, text="Zustellbeginn",width=20,height=5)
StartBtn.grid(row=2,column=0)

ExitBtn = Button(window, text="Exit",width=20,height=5,command=lambda:exit())
ExitBtn.grid(row=2,column=1)

window.mainloop()