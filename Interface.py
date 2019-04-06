import tkinter as tk
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from RNDGraph import get_graph, graph_properties
import matplotlib.pyplot as plt
from matplotlib.figure import SubplotParams
import matplotlib
matplotlib.use("TkAgg")


root = tk.Tk()


class Window:

    def __init__(self, parent):

        self.myParent = parent
        self.main_container = tk.Frame(parent)
        self.main_container.pack(side="top", fill="both", expand=True)

        # Left Frame
        self.left_frame = tk.Frame(self.main_container, width=800, relief="ridge", bd=20, borderwidth=3,
                                   background='white')
        self.left_frame.pack(side="left", fill="both", expand=True)
        self.left_frame.pack_propagate(0)

        # Right Frame
        self.right_frame = tk.Frame(self.main_container, background='black')
        self.right_frame.pack(side="right", fill="both", expand=True)
        self.right_frame.pack_propagate(0)

        # # Right Frame2 - Top
        self.right_frame2_top = tk.Frame(self.right_frame)
        self.right_frame2_top.grid(row=0, column=0, sticky="nsew")
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_propagate(0)

        # LabelFrame - Generate Random Graph
        # FIXME: The font size - not changing
        self.lab_grg = tk.LabelFrame(master=self.right_frame2_top, text="Generate Random Graph", font="10")
        self.lab_grg.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.right_frame2_top.rowconfigure(0, weight=1)
        self.right_frame2_top.columnconfigure(0, weight=1)

        # Label - Number of Vertices
        self.lab_nov = tk.Label(self.lab_grg, text="Number of Vertices:",
                                font="14")
        self.lab_nov.grid(row=1, column=0, pady=5, in_=self.lab_grg)

        # Entry - Number of Vertices
        self.vertices_num = tk.StringVar()
        self.entry_nov = tk.Entry(self.lab_grg, textvariable=self.vertices_num)
        # self.entry_nov.bind('<Return>', self.on_return())
        self.entry_nov.grid(row=1, column=1)
        self.entry_nov.grid_rowconfigure(1, weight=1)

        # Label - Number of Edges
        # FIXME: BUG - Font size not changing
        self.lab_noe = tk.Label(self.lab_grg, text="Number of Edges:",
                                font="14")
        self.lab_noe.grid(row=2, column=0, pady=5, in_=self.lab_grg)

        # Entry - Number of Edges
        self.edges_num = tk.StringVar()
        self.entry_noe = tk.Entry(self.lab_grg, textvariable=self.edges_num)
        # self.entry_nov.bind('<Return>', self.on_return())
        self.entry_noe.grid(row=2, column=1)
        self.entry_noe.grid_rowconfigure(1, weight=1)

        # Button - Generate Random Graph
        self.button_grg = tk.Button(self.lab_grg, text="Generate Graph", bd=3,
                                    command=lambda: get_graph(self))
        self.button_grg.grid(row=3, column=1)
        self.button_grg.grid_rowconfigure(1, weight=1)

        # LabelFrame - Algorithms
        # TODO: BUG - Font size not changing
        self.lab_alg = tk.LabelFrame(self.right_frame2_top, text="Algorithms", font="24")
        self.lab_alg.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.right_frame2_top.rowconfigure(1, weight=1)
        self.right_frame2_top.columnconfigure(0, weight=1)

        # Button - Graph Coloring
        self.button_gc = tk.Button(self.lab_alg, text="Graph Coloring", bd=3)
        self.button_gc.grid(row=0, column=0)
        self.lab_alg.rowconfigure(0, weight=1)
        self.lab_alg.columnconfigure(0, weight=1)

        # LabelFrame - Graph Properties
        self.graph = tk.LabelFrame(self.right_frame2_top, text="Properties", font="24")
        self.graph.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.right_frame2_top.rowconfigure(2, weight=1)
        self.right_frame2_top.columnconfigure(0, weight=1)

        # Button - Print out some graph properties
        self.button_prp = tk.Button(self.graph, text="Graph Properties", bd=3,
                                    command=lambda: graph_properties(self))
        self.button_prp.grid(row=0, column=0)
        self.graph.rowconfigure(0, weight=1)
        self.graph.columnconfigure(0, weight=1)

        # Right Frame2 - Bottom
        self.right_frame2_bottom = tk.Frame(self.right_frame, relief="ridge", bd=20, borderwidth=3)
        self.right_frame2_bottom.grid(row=2, column=0, sticky="nsew")
        self.right_frame.grid_rowconfigure(2, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        # Setting figure properties
        scr_width = root.winfo_screenwidth()
        scr_height = root.winfo_screenheight()
        scr_dpi = root.winfo_fpixels("1i")
        # print("Screen Width: ", scr_width, "Screen Height: ", scr_height, "DPI: ", scr_dpi)

        # Text area to print out the results of the algorithm run
        self.right_frame2_bottom_text = tk.Text(master=self.right_frame2_bottom, relief="ridge",
                                                background="Light Grey", wrap="word", state="normal",
                                                padx=0, pady=0)
        self.right_frame2_bottom_text.pack(side="right", fill="both", expand=True)
        # Adding a scrollbar for the text box.
        # TODO: Scrollbar not working properly
        self.right_frame2_bottom_scr = tk.Scrollbar(master=self.right_frame2_bottom_text)
        self.right_frame2_bottom_scr.pack(side="right", fill="y")
        self.right_frame2_bottom_text.config(state="disabled")

        # Creating the Figure
        fig_num = 1
        self.figure = plt.figure(num=fig_num, figsize=((scr_width / scr_dpi) * 0.6, scr_height / scr_dpi),
                                 clear=True, facecolor="white")
        self.ax = self.figure.add_subplot(111)

        # Defining the canvas
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.left_frame)
        # Defining the toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.left_frame)

    def redirect(self, input_string):

        self.right_frame2_bottom_text.config(state="normal")
        self.right_frame2_bottom_text.insert(tk.INSERT, input_string)
        self.right_frame2_bottom_text.config(state="disabled")

    sys.stdout.write = redirect


# Setting some window properties
root.title("Graph")
# Setting the window size based on the screen size
root.pack_propagate(0)
# # Making the window ful-screen
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# # print(screen_width, " ", screen_height)
# root.geometry("{0}x{1}+0+0".format(screen_width, screen_height))
root.state('zoomed')
# Setting the focus to this window
root.focus_set()
root.update()
# Press the Esc key ends the program
root.bind('<Escape>', lambda e: e.widget.quit())
my_Window = Window(root)
root.mainloop()
