import networkx as nx
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt


class Window:

    def __init__(self, parent):

        self.myParent = parent
        self.main_container = tk.Frame(parent, background="bisque")
        self.main_container.pack(side="top", fill="both", expand=True)

        # Left Frame
        self.left_frame = tk.Frame(self.main_container, background="green")
        self.left_frame.pack(side="left", fill="both", expand=True)

        # Left Frame - Top
        self.left_frame_top = tk.Frame(self.left_frame, background="blue")
        self.left_frame_top.pack(side="top", fill="both", expand=True)

        # Left Frame - Bottom
        self.left_frame_bottom = tk.Frame(self.left_frame, background="red")
        self.left_frame_bottom.pack(side="bottom", fill="both", expand=True)

        # Right Frame
        self.right_frame = tk.Frame(self.main_container, background="yellow")
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.draw_graph()

    # Drawing graph in the top left frame
    # Setting some graph properties
    def draw_graph(self):

        # Embedding the figure
        f = Figure(figsize=(1, 1), dpi=100)
        a = f.add_subplot(111)

        g = nx.path_graph(8)
        pos = nx.spring_layout(g)
        nx.draw(g, pos, ax=a)

        canvas = FigureCanvasTkAgg(f, master=self.left_frame_top)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)


root = tk.Tk()

# Setting some window properties
root.title("Graph")
# Setting the window size based on the screen size
root.pack_propagate(0)
root.update()
screen_width = root.winfo_screenwidth()
print(screen_width)
screen_height = root.winfo_screenheight()
print(screen_height)
print(screen_width, " ", screen_height)
root.geometry('%sx%s' % (screen_width + 1412, screen_height))
root.update()
root.geometry('500x500')
my_Window = Window(root)
root.mainloop()
