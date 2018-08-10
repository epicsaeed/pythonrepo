from tkinter import messagebox, Label, Button,font,Tk,Radiobutton,RIGHT,IntVar,StringVar,Entry,ttk,YES,W, Frame
from tkinter import ttk
import sqlite3
from datetime import datetime

class TourWindow(Frame):

############################################## SET UP FUNCTIONS #############################################
    def __init__(self,parent):
        self.frame = Frame.__init__(self,parent)
        self.parent = parent
        self.parent.title("Tour Menu")
        self.parent.resizable(width=False, height=False)
        self.labelText = StringVar()
        self.labelText.set(self.parent.title())
        self.tour = ""
        self.duration = ""
        self.reason = ""
        self.number = ""
        self.date = ""
        self.line = {"tour":self.tour,"duration":self.duration,"reason":self.reason,"number":self.number,"date":self.date}
        self.setDatabase()
        self.setLabels()
        self.setColumn1()
        self.setColumn2()
        self.setColumn3()
        self.setColumn4()
        self.setTree()
        self.setButtons()
        self.setWrongDelivery()
        
    def setDatabase(self):
        self.connection = sqlite3.connect('tour.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS data(tour TEXT, duration TEXT, reason TEXT, number TEXT, date TEXT)''')
        self.connection.commit()
        self.cursor.execute('DELETE FROM data')
        self.connection.commit()

    def setLabels(self):
        TourLbl = Label(self.frame,text="Tour",font=("Helvetica", 16))
        TourLbl.grid(row=0,column=0)
        TourLbl.config(width=10)
        TourLblFont = font.Font(self.frame, TourLbl.cget("font"))
        TourLblFont.configure(underline=True)
        TourLbl.configure(font=TourLblFont)

        ReasonLbl = Label(self.frame,text="Late Duration",font=("Helvetica", 16))
        ReasonLbl.grid(row=0,column=1)
        ReasonLbl.config(width=10)
        ReasonLblFont = font.Font(ReasonLbl, ReasonLbl.cget("font"))
        ReasonLblFont.configure(underline=True)
        ReasonLbl.configure(font=ReasonLblFont)

        TourLbl2 = Label(self.frame,text="Reason",font=("Helvetica", 16))
        TourLbl2.grid(row=0,column=2)
        TourLbl2.config(width=10)
        TourLbl2Font = font.Font(TourLbl2, TourLbl2.cget("font"))
        TourLbl2Font.configure(underline=True)
        TourLbl2.configure(font=TourLbl2Font)

        NumberLbl = Label(self.frame,text="Number",font=("Helvetica", 16))
        NumberLbl.grid(row=0,column=3,columnspan=2)
        NumberLbl.config(width=10)
        NumberLblFont = font.Font(NumberLbl, NumberLbl.cget("font"))
        NumberLblFont.configure(underline=True)
        NumberLbl.configure(font=NumberLblFont,justify=RIGHT)

    def setColumn1(self):
        column_1_tours = ["Tour1 5:50","Tour2, 6:00","Tour3, 7:00"]
        self.column_1_var = StringVar()
        for val, tour in enumerate(column_1_tours):
            Radiobutton(self.frame,text=tour,indicatoron=0,width=10,padx=10,value=tour,variable=self.column_1_var).grid(row=val+1,column=0)

    def setColumn2(self):
        self.late_var = StringVar()
        self.late_duration = Entry(self.frame,textvariable=self.late_var,width=10)
        self.late_duration.grid(row=1,column=1)
        Label(self.frame,text="ex. 13:00",font=("Helvetica 15 italic")).grid(row=2,column=1)

    def setColumn3(self):
        column_3_reasons = ["verkehrsbedingt","Ausfall Kfz","zu spät vom BZ","zu spät vom PZ","sonstiges"]
        self.column_3_var = StringVar()
        for val, reason in enumerate(column_3_reasons):
            Radiobutton(self.frame,text=reason,indicatoron=0,width=10,padx=10,value=reason,variable=self.column_3_var).grid(row=val+1,column=2)
        self.column_5_text = ["Beh 1 (SKBf)","Beh 2 (GBf)","Beh 3 (MBf)","Rbeh"]

    def setColumn4(self):
        Beh1Lbl = Label(self.frame,text=self.column_5_text[0],justify=RIGHT)
        Beh1Lbl.grid(row=1,column=3)
        Beh1Lbl.config(width=10)
        self.beh1_field = StringVar()
        Beh1Entry = Entry(self.frame,textvariable=self.beh1_field,width=10)
        Beh1Entry.grid(row=1,column=4)

        Beh2Lbl = Label(self.frame,text=self.column_5_text[1],justify=RIGHT)
        Beh2Lbl.grid(row=2,column=3)
        Beh2Lbl.config(width=10)
        self.beh2_field = StringVar()
        Beh2Entry = Entry(self.frame,textvariable=self.beh2_field,width=10)
        Beh2Entry.grid(row=2,column=4)

        Beh3Lbl = Label(self.frame,text=self.column_5_text[2],justify=RIGHT)
        Beh3Lbl.grid(row=3,column=3)
        Beh3Lbl.config(width=10)
        self.beh3_field = StringVar()
        Beh3Entry = Entry(self.frame,textvariable=self.beh3_field,width=10)
        Beh3Entry.grid(row=3,column=4)

        Beh4Lbl = Label(self.frame,text=self.column_5_text[3],justify=RIGHT)
        Beh4Lbl.grid(row=4,column=3)
        Beh4Lbl.config(width=10)
        self.beh4_field = StringVar()
        Beh4Entry = Entry(self.frame,textvariable=self.beh4_field,width=10)
        Beh4Entry.grid(row=4,column=4)

        #puts all fields in a list
        self.fields = [self.beh1_field,self.beh2_field,self.beh3_field,self.beh4_field]

    def setTree(self):
        self.tree = ttk.Treeview(self.frame,height=10,columns=('Late Duration','Reason','Number','Date'),selectmode="extended") 
        self.tree.heading('#0', text="Tour",anchor=W)
        self.tree.heading('#1', text="Late Duration",anchor=W)
        self.tree.heading('#2', text="Reason",anchor=W)
        self.tree.heading('#3', text="Number",anchor=W)
        self.tree.heading('#4', text="Date",anchor=W)
        self.tree.column('#0',stretch=YES,width=15)
        self.tree.column('#1',stretch=YES,width=10)
        self.tree.column('#2',stretch=YES,width=50)
        self.tree.column('#3',stretch=YES,width=50)
        self.tree.column('#4',stretch=YES,width=50)
        self.tree.grid(row=7,columnspan=5,sticky='nsew')
        treeview=self.tree

    def setButtons(self):
        AddBtn = Button(self.frame,text="Add",height=5,width=13,command=lambda:self.add())
        AddBtn.grid(row=8,column=0)

        clrFldBtn = Button(self.frame,text="Clear Fields",height=5,width=13,command=lambda:self.clearFields())
        clrFldBtn.grid(row=8,column=1)

        clrTreeBtn = Button(self.frame,text="Clear Tree",height=5,width=13,command=lambda:self.clearTree())
        clrTreeBtn.grid(row=8,column=2)

        Misc2Btn = Button(self.frame,text="Export",height=5,width=13,command=lambda:self.export())
        Misc2Btn.grid(row=8,column=3)

        ExitBtn = Button(self.frame,text="Submit & Exit",height=5,width=13,command=lambda:exit())
        ExitBtn.grid(row=8,column=4)

    def setWrongDelivery(self):
        #set labels
        FehlLbl = Label(self.frame, text="Fehlerhafte Zuführung",font=("Helvetica",16))
        FehlLbl.grid(row=9,column=0,columnspan=8)
        FehlLbl.config(width=20)
        FehlLblFont = font.Font(FehlLbl,FehlLbl.cget("font"))
        FehlLblFont.configure(underline=True)
        FehlLbl.configure(font=FehlLblFont)
        row = 12
        self.setTableLabels(row)
        self.setTableOneTextFields(row)
        




############################################### HELPER FUNCTIONS #######################################################
    def clearTree(self):
        #clears the treeview + database
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.cursor.execute('DELETE FROM data')
        self.connection.commit()

    def clearFields(self):
        #this functions recieves all checkboxes and text fields in the window and clears them
        self.beh1_field.set("")
        self.beh2_field.set("")
        self.beh3_field.set("")
        self.beh4_field.set("")
        self.late_var.set("")
        self.column_1_var.set("")
        self.column_3_var.set("")

    def add(self):
        #reads radiobutton and fields and add elements to the list box and database
        if self.checkDurationField():
            if self.checkAllNumbersField():
                if self.checkRadiobtns():
                    found = self.getNumberFields()
                    self.line["tour"] = self.column_1_var.get()
                    self.line["duration"] = self.late_duration.get()
                    self.line["reason"] = self.column_3_var.get()
                    self.line["number"] = found
                    self.line["date"] = self.time()
                    if found == "":
                        messagebox.showerror("Error","Characters are not allowed.")
                    else:
                        addedTour = self.line["tour"]
                        addedDuration = self.line["duration"]
                        addedReason = self.line["reason"]
                        addedNumber = self.line["number"]
                        addedTime = self.line["date"]
                        # print(self.line)
                        self.cursor.execute('''INSERT INTO data (tour,duration,reason,number,date) VALUES(?,?,?,?,?)''',(addedTour,addedDuration,addedReason,addedNumber,addedTime))
                        self.connection.commit()
                        self.tree.insert("",0,text=addedTour,values=(addedDuration,addedReason,addedNumber,addedTime))
                else:
                    messagebox.showerror("Error","Please select atleast one button from each column")
            else:
                messagebox.showerror("Error","All Number fields are empty.")
        else:
            messagebox.showerror("Error","Please insert valid duration value. (00:00)")

    def getNumberFields(self):
        #returns the non-empty values of the number column as a string
        allfields = [self.beh1_field.get(),self.beh2_field.get(),self.beh3_field.get(),self.beh4_field.get()]
        found = ""
        for i in range(4):
            # print(allfields[i].isdigit())
            if allfields[i] != "" and self.checkIndivisualField(self.fields[i]):
                found+=self.column_5_text[i]+"="+str(allfields[i])+", "
            else:
                continue
        # print(found)
        return found[:-2]

    def dict_factory(self,row):
        d = {}
        for idx,col in enumerate(self.cursor.description):
            d[col[0]] = row[idx]
        return d

    def view(self):
        self.connection.row_factory = self.dict_factory
        view = self.cursor.execute('SELECT * FROM data').fetchall()
        return view

    def export(self):
        #exports the treeview list into a csv. file
        import csv
        exportedFile = "tour.csv"
        data = self.view()
        list = [[]]
        for i in range(len(data)):
            list = list + [[data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]]]
            print(list)
        with open(exportedFile,"w",newline='') as output:
            a = csv.writer(output,delimiter=',')
            headline = [['Tour','Late Duration','Reason','Number','Date Created'],]
            a.writerows(headline)
            del list[0]
            a.writerows(list)
            self.runFile("tour.csv")

    def runFile(self,filename):
        #opens the exported file
        import os,subprocess
        try:
            os.startfile(filename)
        except AttributeError:
            subprocess.call(['open', filename])

    def setTableLabels(self,row):
        Label(self.frame, text="falsche Infoträger").grid(row=row-2,column=0,columnspan=8)
        Label(self.frame, text="E+1").grid(row=row-1,column=2)
        Label(self.frame, text="E+2/4").grid(row=row-1,column=6)

        #set headers
        header_text = ["Beh 1 (SKBf)","Beh 2 (GMBF)","Beh 3 MBf"]
        for i in range(3):
            Label(self.frame, text=header_text[i]).grid(row=row,column=i+1)
        for i in range(3):
            Label(self.frame, text=header_text[i]).grid(row=row,column=i+5)

        #set row labels
        row_text = ["Laufzeit","eingehalten","verzögert","unbekannt","für PLZ, ZSP"]
        #row+=1
        count = row
        for labels in row_text:
            Label(self.frame,text=labels).grid(column=0,row=count)
            count+=1

    def setTableOneTextFields(self,row):
        #set text fields
        self.r13c1Var = StringVar()
        self.r13c1Entry = Entry(self.frame,textvariable=self.r13c1Var,width=10)
        self.r13c1Entry.grid(row=row+1,column=1)

        self.r14c1Var = StringVar()
        self.r14c1Entry = Entry(self.frame,textvariable=self.r14c1Var,width=10)
        self.r14c1Entry.grid(row=row+2,column=1)

        self.r15c1Var = StringVar()
        self.r15c1Entry = Entry(self.frame,textvariable=self.r15c1Var,width=10)
        self.r15c1Entry.grid(row=row+3,column=1)

        self.r16c1Var = StringVar()
        self.r16c1Entry = Entry(self.frame,textvariable=self.r16c1Var,width=10)
        self.r16c1Entry.grid(row=row+4,column=1)

        self.r13c2Var = StringVar()
        self.r13c2Entry = Entry(self.frame,textvariable=self.r13c2Var,width=10)
        self.r13c2Entry.grid(row=row+1,column=2)

        self.r14c2Var = StringVar()
        self.r14c2Entry = Entry(self.frame,textvariable=self.r14c2Var,width=10)
        self.r14c2Entry.grid(row=row+2,column=2)

        self.r15c2Var = StringVar()
        self.r15c2Entry = Entry(self.frame,textvariable=self.r15c2Var,width=10)
        self.r15c2Entry.grid(row=row+3,column=2)

        self.r16c2Var = StringVar()
        self.r16c2Entry = Entry(self.frame,textvariable=self.r16c2Var,width=10)
        self.r16c2Entry.grid(row=row+4,column=2)

        self.r13c3Var = StringVar()
        self.r13c3Entry = Entry(self.frame,textvariable=self.r13c3Var,width=10)
        self.r13c3Entry.grid(row=row+1,column=3)

        self.r14c3Var = StringVar()
        self.r14c3Entry = Entry(self.frame,textvariable=self.r14c3Var,width=10)
        self.r14c3Entry.grid(row=row+2,column=3)

        self.r15c3Var = StringVar()
        self.r15c3Entry = Entry(self.frame,textvariable=self.r15c3Var,width=10)
        self.r15c3Entry.grid(row=row+3,column=3)

        self.r16c3Var = StringVar()
        self.r16c3Entry = Entry(self.frame,textvariable=self.r16c3Var,width=10)
        self.r16c3Entry.grid(row=row+4,column=3)

        self.r13c5Var = StringVar()
        self.r13c5Entry = Entry(self.frame,textvariable=self.r13c5Var,width=10)
        self.r13c5Entry.grid(row=row+1,column=5)

        self.r14c5Var = StringVar()
        self.r14c5Entry = Entry(self.frame,textvariable=self.r14c5Var,width=10)
        self.r14c5Entry.grid(row=row+2,column=5)

        self.r15c5Var = StringVar()
        self.r15c5Entry = Entry(self.frame,textvariable=self.r15c5Var,width=10)
        self.r15c5Entry.grid(row=row+3,column=5)

        self.r16c5Var = StringVar()
        self.r16c5Entry = Entry(self.frame,textvariable=self.r16c5Var,width=10)
        self.r16c5Entry.grid(row=row+4,column=5)

        self.r13c6Var = StringVar()
        self.r13c6Entry = Entry(self.frame,textvariable=self.r13c6Var,width=10)
        self.r13c6Entry.grid(row=row+1,column=6)

        self.r14c6Var = StringVar()
        self.r14c6Entry = Entry(self.frame,textvariable=self.r14c6Var,width=10)
        self.r14c6Entry.grid(row=row+2,column=6)

        self.r15c6Var = StringVar()
        self.r15c6Entry = Entry(self.frame,textvariable=self.r15c6Var,width=10)
        self.r15c6Entry.grid(row=row+3,column=6)

        self.r16c6Var = StringVar()
        self.r16c6Entry = Entry(self.frame,textvariable=self.r16c6Var,width=10)
        self.r16c6Entry.grid(row=row+4,column=6)

        self.r13c7Var = StringVar()
        self.r13c7Entry = Entry(self.frame,textvariable=self.r13c7Var,width=10)
        self.r13c7Entry.grid(row=row+1,column=7)

        self.r14c7Var = StringVar()
        self.r14c7Entry = Entry(self.frame,textvariable=self.r14c7Var,width=10)
        self.r14c7Entry.grid(row=row+2,column=7)

        self.r15c7Var = StringVar()
        self.r15c7Entry = Entry(self.frame,textvariable=self.r15c7Var,width=10)
        self.r15c7Entry.grid(row=row+3,column=7)

        self.r16c7Var = StringVar()
        self.r16c7Entry = Entry(self.frame,textvariable=self.r16c7Var,width=10)
        self.r16c7Entry.grid(row=row+4,column=7)






    @staticmethod
    def time():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

############################################### ERROR CHECKING FUNCTIONS ###############################################

    def checkDurationField(self):
        #checks if duration field of the format 00:00
        time = str(self.late_var.get())
        if len(time) == 5:
            try:
                if (time[0:2]+time[3:5]).isdigit() and time[2] == ':':
                    return True
            except AttributeError:
                return False
        return False

    @staticmethod
    def checkIndivisualField(entry):
        #returns true if the passed field is a digit
        return entry.get().isdigit()

    def checkAllNumbersField(self):
        #returns False if all numbers fields are empty
        if self.beh1_field.get() == "" and self.beh2_field.get() == "" and self.beh3_field.get() == "" and self.beh4_field.get() == "":
            return False
        return True

    def checkRadiobtns(self):
        #returns False is neither radiobuttons are selected
        if str(self.column_1_var.get()) != "" and str(self.column_3_var.get()) != "":
            return True
        return False

def main():
    root = Tk()
    app = TourWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()

