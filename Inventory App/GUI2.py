import tkinter as tk

LARGE_FONT = ("Verdana",12)

class InventoryApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage,MainPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Choose the import source from the buttons below:",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        txt = tk.Button(self, text="Import from txt file",command=lambda: controller.show_frame(MainPage))
        txt.pack()

        db = tk.Button(self, text="Import from database",command=lambda: controller.show_frame(MainPage))
        db.pack()

        close = tk.Button(self, text="Exit",command=quit)
        close.pack()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Page One",font=LARGE_FONT)
        label.pack(pady=10,padx=10)


app = InventoryApp()
app.mainloop()