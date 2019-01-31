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

        # Left Frame - Bottom2
        self.left_frame_bottom2 = tk.Frame(self.left_frame_bottom, background="orange")
        self.left_frame_bottom2.pack(side="bottom", fill="both", expand=True)

        # Text area to print out the results of the algorithm run
        # FIXME: This makes the top and bottom frames resize, making the top frame smaller
        # This happens only when Text is used. Label is fine
        self.left_frame_bottom2_text = tk.Label(self.left_frame_bottom2, background="black")
        self.left_frame_bottom2_text.pack(side="bottom", fill="both", expand=True)

        # Right Frame
        self.right_frame = tk.Frame(self.main_container, background="yellow")
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Right Frame2
        self.right_frame2 = tk.Frame(self.right_frame, background="pink")
        self.right_frame2.pack(side="right", fill="both", expand=True)

        # Right Frame2 - Top
        self.right_frame2_top = tk.Frame(self.right_frame2, relief="ridge", background="bisque", bd=20, borderwidth=3,
                                         padx=5, pady=5)
        self.right_frame2_top.grid(row=0, column=0, sticky="nsew")
        self.right_frame2.grid_rowconfigure(4, weight=1)
        self.right_frame2.grid_columnconfigure(0, weight=1)

        # Label - Generate Random Graph
        # FIXME: The font size - not changing
        self.lab_grg = tk.Label(self.right_frame2_top, text="Generate Random Graph",
                                font="24")
        self.lab_grg.grid(row=0, column=0, padx=10, pady=10, in_=self.right_frame2_top)

        # Label - Number of Vertices
        self.lab_nov = tk.Label(self.right_frame2_top, text="Number of Vertices:",
                                font="14")
        self.lab_nov.grid(row=1, column=0, pady=5, in_=self.right_frame2_top)

        # Entry - Number of Vertices
        num_vertices = tk.StringVar()
        self.entry_nov = tk.Entry(self.right_frame2_top, textvariable=num_vertices)
        self.entry_nov.grid(row=1, column=1)
        self.entry_nov.grid_rowconfigure(1, weight=1)

        def prn():

            a = num_vertices.get()
            print("Number should be here ->" + a)

        # Button - Generate Random Graph
        # TODO: Add the lambda command to generate the graph based on the number of vertices entered
        self.button_grg = tk.Button(self.right_frame2_top, text="Generate Graph", bd=3,
                                    command=prn())
        self.button_grg.grid(row=2, column=1)
        self.button_grg.grid_rowconfigure(1, weight=1)

        # TODO: Border the generate random graph section

        self.draw_graph()

    # # Get the input from the entry
    # def rnd_graph(self):
    #

    # Drawing graph in the top left frame
    def draw_graph(self):

        # Embedding the figure
        f = Figure(figsize=(1, 1), dpi=100)
        a = f.add_subplot(111)

        g = nx.path_graph(8)
        pos = nx.spring_layout(g)
        nx.draw(g, pos, ax=a)

        canvas = FigureCanvasTkAgg(f, master=self.left_frame_top)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    # TODO: a random graph method which draws the graph
    # Get the number of vertices entered by the user and draw a
    # random graph based on the number
    # def random_graph(self):





root = tk.Tk()

# Setting some window properties
root.title("Graph")
# Setting the window size based on the screen size
root.pack_propagate(0)
# Making the window fullscreen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width, " ", screen_height)
root.geometry("{0}x{1}+0+0".format(screen_width, screen_height))
# Setting the focus to this window
root.focus_set()
root.update()
# Press the Esc key ends the program
root.bind('<Escape>', lambda e: e.widget.quit())
my_Window = Window(root)
root.mainloop()
