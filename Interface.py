import networkx as nx
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

root = tk.Tk()

class Window:

    def __init__(self, parent):

        self.myParent = parent
        self.main_container = tk.Frame(parent)
        self.main_container.pack(side="top", fill="both", expand=True)

        # Left Frame
        self.left_frame = tk.Frame(self.main_container)
        self.left_frame.pack(side="left", fill="both", expand=True)

        # Left Frame - Top
        self.left_frame_top = tk.Frame(self.left_frame, relief="ridge", bd=20, borderwidth=3, pady=2, padx=2)
        self.left_frame_top.pack(side="top", fill="both", expand=True)

        # Left Frame - Bottom
        self.left_frame_bottom = tk.Frame(self.left_frame)
        self.left_frame_bottom.pack(side="bottom", fill="both", expand=True)

        # Left Frame - Bottom2
        self.left_frame_bottom2 = tk.Frame(self.left_frame_bottom)
        self.left_frame_bottom2.pack(side="bottom", fill="both", expand=True)

        # Text area to print out the results of the algorithm run
        # FIXME: This makes the top and bottom frames resize, making the top frame smaller
        # This happens only when Text is used. Label is fine
        self.left_frame_bottom2_text = tk.Label(self.left_frame_bottom2)
        self.left_frame_bottom2_text.pack(side="bottom", fill="both", expand=True)

        # Right Frame
        self.right_frame = tk.Frame(self.main_container)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Right Frame2
        self.right_frame2 = tk.Frame(self.right_frame)
        self.right_frame2.pack(side="right", fill="both", expand=True)

        # Right Frame2 - Top
        self.right_frame2_top = tk.Frame(self.right_frame2, relief="ridge", bd=20, borderwidth=3,
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
        self.vertices_num = tk.StringVar()
        self.entry_nov = tk.Entry(self.right_frame2_top, textvariable=self.vertices_num)
        # self.entry_nov.bind('<Return>', self.on_return())
        self.entry_nov.grid(row=1, column=1)
        self.entry_nov.grid_rowconfigure(1, weight=1)

        # Label - Number of Edges
        # FIXME: The font size - not changing
        self.lab_noe = tk.Label(self.right_frame2_top, text="Number of Edges:",
                                font="14")
        self.lab_noe.grid(row=2, column=0, pady=5, in_=self.right_frame2_top)

        # Entry - Number of Edges
        self.edges_num = tk.StringVar()
        self.entry_noe = tk.Entry(self.right_frame2_top, textvariable=self.edges_num)
        # self.entry_nov.bind('<Return>', self.on_return())
        self.entry_noe.grid(row=2, column=1)
        self.entry_noe.grid_rowconfigure(1, weight=1)

        # Button - Generate Random Graph
        self.button_grg = tk.Button(self.right_frame2_top, text="Generate Graph", bd=3,
                                    command=lambda: self.get_vertices())
        self.button_grg.grid(row=3, column=1)
        self.button_grg.grid_rowconfigure(1, weight=1)

        # self.draw_graph()

    # def on_return(self):
    #     print("Return Pressed")
    #     self.entry_nov.delete(0, 'end')

    # Getting the number of vertices for the random graph
    # Performs validation checks on the user input to make sure the input entered is correct
    # TODO: Add a upper limit to the input validation
    # FIXME: A new graph is drawn every time underneath the old one
    def get_vertices(self):

        string_vertices = self.vertices_num.get()
        string_edges = self.edges_num.get()

        try:
            num_vertices = int(string_vertices)
            print("Vertices number value is: ", num_vertices)

            num_edges = int(string_edges)
            print("Edges number value is: ", num_edges)

            # TODO: Improve error handling
            if num_vertices >= 2 and num_edges >= 1:
                print("DRAW THE GRAPH NOW")
                self.draw_graph(num_vertices, num_edges)
            elif 0 < num_vertices < 2:
                print("The graph must contain at least 2 vertices")
                messagebox.showerror("VERTEX INPUT ERROR", "The graph must contain at least 2 vertices.")
            elif num_vertices < 0:
                print("The minimum number of vertices cannot be a negative number.")
                messagebox.showerror("VERTEX INPUT ERROR", "The minimum number of vertices cannot be a negative number.")
            elif 0 <= num_edges < 1:
                print("The graph must contain at least 1 edge")
                messagebox.showerror("EDGE INPUT ERROR", "The graph must contain at least 1 edge.")
            elif num_edges < 0:
                print("The minimum number of edges cannot be a negative number.")
                messagebox.showerror("EDGE INPUT ERROR", "The minimum number of edges cannot be a negative number.")
        except ValueError:
            print("Entered value is not a number")
            messagebox.showerror("INPUT ERROR", "A number must be entered.")

    # Drawing graph in the top left frame
    def draw_graph(self, vertices, edges):

        # Delete the previous graph

        # Embedding the figure
        f = Figure(figsize=(1.5, 1.5), dpi=100)
        a = f.add_subplot(111)

        g = nx.dense_gnm_random_graph(vertices, edges)
        pos = nx.spring_layout(g)
        nx.draw(g, pos, ax=a)

        canvas = FigureCanvasTkAgg(f, master=self.left_frame_top)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)


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
