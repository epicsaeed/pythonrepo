from tkinter import *
from tkinter import ttk
import tour

class MainMenu(Frame):
    def __init__(self,parent):
        self.frame = Frame.__init__(self,parent)
        self.parent = parent
        self.parent.resizable(width=False, height=False)
        self.parent.title("Support App Main Menu")
        self.labelText = StringVar()
        self.labelText.set(self.parent.title())
        self.loadView()

    def loadView(self):
        TourBtn = Button(self.frame, text="Tour",width=20,height=5,command=self.tour_window)
        TourBtn.grid(row=0,column=0)

        WrongDepotBtn = Button(self.frame, text="Fehlerhafte Zuführung",width=20,height=5)
        WrongDepotBtn.grid(row=0,column=1)

        LeftoverBtn = Button(self.frame, text="Rückstände im ZSP",width=20,height=5)
        LeftoverBtn.grid(row=1,column=0)

        InfoBtn = Button(self.frame, text="sonstige Informationen",width=20,height=5)
        InfoBtn.grid(row=1,column=1)

        StartBtn = Button(self.frame, text="Zustellbeginn",width=20,height=5)
        StartBtn.grid(row=2,column=0)

        ExitBtn = Button(self.frame, text="Exit",width=20,height=5,command=lambda:exit())
        ExitBtn.grid(row=2,column=1)

    def tour_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = tour.TourWindow(self.newWindow)






def main():
    root = Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()

