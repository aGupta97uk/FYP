import tkinter as tk
from tkinter import *


class window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master


root = Tk()

app = window(root)

root.mainloop()
