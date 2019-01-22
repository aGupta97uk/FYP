import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure


class Window(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)

        container = tk.Frame(self)

        container.grid_rowconfigure(10, weight=1)
        container.grid_columnconfigure(10, weight=1)

        # Label
        lab = tk.Label(self, text="Label")
        lab.grid(row=5, column=5)

        # Button
        button1 = ttk.Button(self, text="Button 1")
        button1.grid(row=1, column=1)

        # Figure
        fig = Figure(figsize=(5, 5), dpi=100)
        a = fig.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 6])

        # Embedding the figure into the canvas
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)


root = Window()
root.mainloop()
