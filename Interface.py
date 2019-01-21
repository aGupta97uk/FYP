import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):

    def __init__(self):
        # self.tk = Tk()

        tk.Tk.__init__(self)
        tk.Tk.iconbitmap(self)
        tk.Tk.wm_title(self)

        container = tk.Frame(self)

        container.grid_rowconfigure(10, weight=1)
        container.grid_columnconfigure(10, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        # Label
        lab = tk.Label(self, text="StartPage")
        lab.grid(row=3, column=5)

        # Button
        button1 = ttk.Button(self, text="Button1", command=lambda: controller.show_frame(PageOne))
        button1.grid(row=1, column=1)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Label
        lab = tk.Label(self, text="PageOne")
        lab.grid(row=3, column=5)

        # Button
        button1 = ttk.Button(self, text="Button1", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1)


root = Window()
root.mainloop()
