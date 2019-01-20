import tkinter as tk
from tkinter import *


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,  *args, **kwargs)

        container = tk.Frame(self)
        container.pack()
        container.grid_rowconfigure()
        container.grid_columnconfigure()

        frame = F(container, self)
        self.frame[F] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text = "Graph", font=("Helvetica", 12))
        label.pack(pady=10, padx=10)


root = Window()
root.mainloop()
