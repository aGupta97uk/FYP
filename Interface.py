import tkinter as tk
import sys
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter.scrolledtext import ScrolledText
from RNDGraph import get_graph, graph_properties
from GraphColoring import get_gc, check_num_colors_answer
import matplotlib.pyplot as plt
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
        self.right_frame = tk.Frame(self.main_container)
        self.right_frame.pack(side="right", fill="both", expand=True)
        self.right_frame.pack_propagate(0)

        # # Right Frame2 - Top
        self.right_frame2_top = tk.Frame(self.right_frame, relief="ridge", bd=20, borderwidth=3)
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
        self.lab_nov.grid(row=1, column=0, pady=5, in_=self.lab_grg, sticky="e")

        # Entry - Number of Vertices
        self.vertices_num = tk.StringVar()
        self.vertices_num.set("Min: 2, Max: 8")
        self.entry_nov = tk.Entry(self.lab_grg, textvariable=self.vertices_num, foreground="#828282")
        self.entry_nov.bind("<Button-1>", lambda e: self.clear_text(self.entry_nov))
        self.entry_nov.grid(row=1, column=1)
        self.entry_nov.grid_rowconfigure(1, weight=1)

        # Label - Number of Edges
        # FIXME: BUG - Font size not changing
        self.lab_noe = tk.Label(self.lab_grg, text="Number of Edges:",
                                font="14")
        self.lab_noe.grid(row=2, column=0, pady=5, in_=self.lab_grg, sticky="e")

        # Entry - Number of Edges
        self.edges_num = tk.StringVar()
        self.edges_num.set("Min: 1, Max: 28")
        self.entry_noe = tk.Entry(self.lab_grg, textvariable=self.edges_num, foreground="#828282")
        self.entry_noe.bind("<Button-1>", lambda x: self.clear_text(self.entry_noe))
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
        self.button_gc = tk.Button(self.lab_alg, text="Graph Coloring", bd=3,
                                   command=lambda: self.graph_coloring())
        self.button_gc.grid(row=0, column=0)
        self.lab_alg.rowconfigure(0, weight=1)
        self.lab_alg.columnconfigure(0, weight=1)

        # LabelFrame - Graph Properties
        self.lab_prop = tk.LabelFrame(self.right_frame2_top, text="Properties", font="24")
        self.lab_prop.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.right_frame2_top.rowconfigure(2, weight=1)
        self.right_frame2_top.columnconfigure(0, weight=1)

        # Button - Print out some graph properties
        self.button_prp = tk.Button(self.lab_prop, text="Graph Properties", bd=3,
                                    command=lambda: graph_properties(self))
        self.button_prp.grid(row=0, column=0)
        self.lab_prop.rowconfigure(0, weight=1)
        self.lab_prop.columnconfigure(0, weight=1)

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
        # Using the ScrolledText widget because from python 3.0 onwards this is available which is very useful.
        self.right_frame2_bottom_text = tk.scrolledtext.ScrolledText(master=self.right_frame2_bottom, relief="ridge",
                                                                     background="Light Grey", wrap="word",
                                                                     state="normal", padx=0, pady=0)
        self.right_frame2_bottom_text.pack(side="right", fill="both", expand=True)
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

    def graph_coloring(self):

        self.right_frame2_top.grid_forget()

        self.right_frame2_top_gc = tk.Frame(self.right_frame, relief="ridge", bd=20, borderwidth=3)
        self.right_frame2_top_gc.grid(row=0, column=0, sticky="nsew")
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_propagate(0)

        # Back Button
        self.button_bck = tk.Button(self.right_frame2_top_gc, text="Back", bd=3,
                                    command=lambda: self.back())
        self.button_bck.grid(row=0, sticky="e", padx=10, pady=0)

        # Main Code for Graph coloring UI
        self.lab_gc = tk.LabelFrame(self.right_frame2_top_gc, text="Graph Coloring", font="24")
        self.lab_gc.grid(row=1, column=0, padx=10, pady=(0, 10), rowspan=5, sticky="nsew")
        self.right_frame2_top_gc.rowconfigure(1, weight=1)
        self.right_frame2_top_gc.columnconfigure(0, weight=1)
        self.lab_gc.grid_propagate(False)

        # Make this create a new Window and present the algorithm in that window
        self.btn_info = tk.Button(self.lab_gc, text="How it works", bd=3, command=lambda: self.how_it_works())
        self.btn_info.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.lab_gc.rowconfigure(0, weight=1)
        self.lab_gc.columnconfigure(0, weight=1)

        # Button to execute the graph coloring algorithm on the existing graph
        self.btn_gc = tk.Button(self.lab_gc, text="Run Algorithm", bd=3,
                                command=lambda: get_gc(self))
        self.btn_gc.grid(row=5, column=5, padx=10, pady=10, sticky="e")
        self.lab_gc.rowconfigure(0, weight=1)
        self.lab_gc.columnconfigure(0, weight=1)

        # Container
        self.container = tk.Frame(self.lab_gc)
        self.container.grid(row=0, column=0, rowspan=4, columnspan=6, padx=10, pady=10, sticky="nsew")
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        # Label
        # TODO: Not all text is visible in the label
        self.lab_num_colors = tk.Label(self.container, text="How many colours do you think it will "
                                                            "take to color all vertices in this graph?",
                                       font=12)
        self.lab_num_colors.pack(side="top", anchor="nw", fill="both", expand=False)
        self.lab_num_colors.pack_propagate(0)

        # Entry
        self.entry_num_colors = tk.Entry(self.container)
        self.entry_num_colors.pack(side="top", anchor="n", padx=10, pady=10)

        # Button
        self.button_num_colors = tk.Button(self.container, text="Check Answer",
                                           command=lambda: check_num_colors_answer(self))
        self.button_num_colors.pack(side="top", anchor="n", padx=10, pady=10)

    def back(self):

        self.right_frame2_top_gc.grid_forget()

        # Repeated Code here. Find a better way to do grid (remember)
        self.right_frame2_top.grid(row=0, column=0, sticky="nsew")
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_propagate(0)

    def redirect(self, input_string):

        self.right_frame2_bottom_text.config(state="normal")
        self.right_frame2_bottom_text.insert(tk.INSERT, input_string)
        self.right_frame2_bottom_text.config(state="disabled")

    sys.stdout.write = redirect

    def clear_text(self, event):

        if event == self.entry_nov:
            self.entry_nov.delete(0, 'end')
            self.entry_nov.configure(foreground="black")
        else:
            self.entry_noe.delete(0, 'end')
            self.entry_noe.configure(foreground="black")

    def how_it_works(self):

        graph_coloring = tk.Toplevel()

        def close_window():
            graph_coloring.destroy()

        graph_coloring.title("Welsh Powell Algorithm")
        graph_coloring.state('zoomed')
        graph_coloring.focus_force()

        self.main_container = tk.Frame(graph_coloring, background="green")
        self.main_container.pack(side="top", fill="both", expand=True)

        self.button_quit = tk.Button(self.main_container, text="Quit", bd=3, command=lambda: close_window())
        self.button_quit.pack(side="top", anchor="e", padx=10, pady=(10, 0))

        alg_lab = "Welsh Powell Algorithm"
        self.alg_text = tk.Message(self.main_container, text=alg_lab, width=500, font=60, background="grey")
        self.alg_text.pack(side="top", anchor="center", fill="both", padx=10, pady=10)

        alg = 'Step 1: Find the degree of each vertex.\n' \
              'Step 2: List the vertices in descending order of degrees.\n' \
              'Step 3: Color the first vertex in the list.\n' \
              'Step 4: Go down the vertex list and color every vertex not connected\n' \
              "              "'to the colored vertex with the same color.\n' \
              'Step 5: Repeat step 3 and 4 with a new colour until all vertices are\n' \
              "              "'colored.'
        self.alg = tk.Message(self.main_container, text=alg, width=500, font=30,
                              background="light grey", justify="left")
        self.alg.pack(side="top", anchor="center", fill="both", padx=10, pady=10)

        self.demo_lab = tk.Label(self.main_container, text="Demo", width=500, font=60, background="grey")
        self.demo_lab.pack(side="top", anchor="center", fill="both", padx=10, pady=10)

        # Canvas for the image
        self.left = tk.Frame(self.main_container, background="blue")
        self.left.pack(side="left", anchor="center", fill="both", padx=10, pady=10, expand=True)

        # Graph Image Canvas---------------------------------------------------------------------
        self.graph_canvas = tk.Canvas(self.left, background="brown")
        self.graph_canvas.pack(side="top", fill="both", expand=True)

        self.right = tk.Frame(self.main_container, background="white")
        self.right.pack(side="right", anchor="center", fill="both", padx=10, pady=10, expand=True)

        # Explanation Area----------------------------------------------------------------------
        self.exp = tk.Frame(self.right, background="purple")
        self.exp.pack(side="top", anchor="center", fill="both", expand=True)

        # Button to show the images in an order
        self.button_step_one = tk.Button(self.exp, text="Step 1", bd=3, command=lambda: self.step_one())
        self.button_step_one.pack(side="left", anchor="n", padx=10, pady=10, expand=True)

        self.button_step_two = tk.Button(self.exp, text="Step 2", bd=3, command=lambda: self.step_two())
        self.button_step_two.pack(side="left", anchor="n", padx=10, pady=10, expand=True)

        # Edit
        self.button_step_three = tk.Button(self.exp, text="Step 3", bd=3, command=lambda: self.step_three())
        self.button_step_three.pack(side="left", anchor="n", padx=10, pady=10, expand=True)

        self.button_step_four = tk.Button(self.exp, text="Step 4", bd=3, command=lambda: self.step_four())
        self.button_step_four.pack(side="left", anchor="n", padx=10, pady=10, expand=True)

        self.button_step_five = tk.Button(self.exp, text="Step 5", bd=3, command=lambda: self.step_five())
        self.button_step_five.pack(side="left", anchor="n", padx=10, pady=10, expand=True)

        self.button_step_six = tk.Button(self.exp, text="Step 6", bd=3, command=lambda: self.step_six())
        self.button_step_six.pack(side="left", anchor="n", padx=10, pady=10, expand=True)

        self.button_step_seven = tk.Button(self.exp, text="Step 7", bd=3, command=lambda: self.step_seven())
        self.button_step_seven.pack(side="left", anchor="n", padx=10, pady=10, expand=True)

        self.button_step_eight = tk.Button(self.exp, text="Step 8", bd=3, command=lambda: self.step_eight())
        self.button_step_eight.pack(side="left", anchor="n", padx=10, pady=10, expand=True)

        # Adjacency Matrix Image Canvas---------------------------------------------------------
        self.adj_matrix_canvas = tk.Canvas(self.right, background="blue")
        self.adj_matrix_canvas.pack(side="bottom", anchor="center", fill="both", expand=True)

        graph_coloring.mainloop()

    # A method which displays the images in the canvas.
    def step_one(self):

        global left_height
        left_height = self.left.winfo_height()

        global left_width
        left_width = self.left.winfo_width()

        global right_height
        right_height = self.adj_matrix_canvas.winfo_height()

        global right_width
        right_width = self.adj_matrix_canvas.winfo_width()

        # Loading all the graph images
        load_graph_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/Graphv1.0.gif")
        # Get frame size
        load_graph_image = load_graph_image.resize((left_width, left_height))

        # Loading adjacency matrix images
        load_adj_mat_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/AdjacencyMatrixv1.0.gif")
        # Get frame size
        load_adj_mat_image = load_adj_mat_image.resize((right_width, right_height))

        # Render graph Images
        self.render_graph = ImageTk.PhotoImage(load_graph_image)
        # Displaying the graph image
        self.img_graph = tk.Label(self.left, image=self.render_graph)
        self.img_graph.image = self.render_graph
        self.img_graph.place(x=0, y=0)

        # Render Adjacency matrix images
        self.render_adj_matrix = ImageTk.PhotoImage(load_adj_mat_image)
        # Displaying the adjacency matrix images
        self.img_adj_matrix = tk.Label(self.adj_matrix_canvas, image=self.render_adj_matrix)
        self.img_adj_matrix.image = self.render_adj_matrix
        self.img_adj_matrix.place(x=0, y=0)

        return self.render_graph, self.render_adj_matrix

    def step_two(self):

        global left_height
        left_height = self.left.winfo_height()

        global left_width
        left_width = self.left.winfo_width()

        global right_height
        right_height = self.adj_matrix_canvas.winfo_height()

        global right_width
        right_width = self.adj_matrix_canvas.winfo_width()

        # Loading all the graph images
        load_graph_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/Graphv2.0.gif")
        # Get frame size
        load_graph_image = load_graph_image.resize((left_width, left_height))

        # Loading adjacency matrix images
        load_adj_mat_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/AdjacencyMatrixv2.0.gif")
        # Get frame size
        load_adj_mat_image = load_adj_mat_image.resize((right_width, right_height))

        # Render graph Images
        self.render_graph = ImageTk.PhotoImage(load_graph_image)
        # Displaying the graph image
        self.img_graph = tk.Label(self.left, image=self.render_graph)
        self.img_graph.image = self.render_graph
        self.img_graph.place(x=0, y=0)

        # Render Adjacency matrix images
        self.render_adj_matrix = ImageTk.PhotoImage(load_adj_mat_image)
        # Displaying the adjacency matrix images
        self.img_adj_matrix = tk.Label(self.adj_matrix_canvas, image=self.render_adj_matrix)
        self.img_adj_matrix.image = self.render_adj_matrix
        self.img_adj_matrix.place(x=0, y=0)

        return self.render_graph, self.render_adj_matrix

    def step_three(self):

        global left_height
        left_height = self.left.winfo_height()

        global left_width
        left_width = self.left.winfo_width()

        global right_height
        right_height = self.adj_matrix_canvas.winfo_height()

        global right_width
        right_width = self.adj_matrix_canvas.winfo_width()

        # Loading all the graph images
        load_graph_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/Graphv3.0.gif")
        # Get frame size
        load_graph_image = load_graph_image.resize((left_width, left_height))

        # Loading adjacency matrix images
        load_adj_mat_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/AdjacencyMatrixv3.0.gif")
        # Get frame size
        load_adj_mat_image = load_adj_mat_image.resize((right_width, right_height))

        # Render graph Images
        self.render_graph = ImageTk.PhotoImage(load_graph_image)
        # Displaying the graph image
        self.img_graph = tk.Label(self.left, image=self.render_graph)
        self.img_graph.image = self.render_graph
        self.img_graph.place(x=0, y=0)

        # Render Adjacency matrix images
        self.render_adj_matrix = ImageTk.PhotoImage(load_adj_mat_image)
        # Displaying the adjacency matrix images
        self.img_adj_matrix = tk.Label(self.adj_matrix_canvas, image=self.render_adj_matrix)
        self.img_adj_matrix.image = self.render_adj_matrix
        self.img_adj_matrix.place(x=0, y=0)

        return self.render_graph, self.render_adj_matrix

    def step_four(self):

        global left_height
        left_height = self.left.winfo_height()

        global left_width
        left_width = self.left.winfo_width()

        global right_height
        right_height = self.adj_matrix_canvas.winfo_height()

        global right_width
        right_width = self.adj_matrix_canvas.winfo_width()

        # Loading all the graph images
        load_graph_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/Graphv4.0.gif")
        # Get frame size
        load_graph_image = load_graph_image.resize((left_width, left_height))

        # Loading adjacency matrix images
        load_adj_mat_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/AdjacencyMatrixv4.0.gif")
        # Get frame size
        load_adj_mat_image = load_adj_mat_image.resize((right_width, right_height))

        # Render graph Images
        self.render_graph = ImageTk.PhotoImage(load_graph_image)
        # Displaying the graph image
        self.img_graph = tk.Label(self.left, image=self.render_graph)
        self.img_graph.image = self.render_graph
        self.img_graph.place(x=0, y=0)

        # Render Adjacency matrix images
        self.render_adj_matrix = ImageTk.PhotoImage(load_adj_mat_image)
        # Displaying the adjacency matrix images
        self.img_adj_matrix = tk.Label(self.adj_matrix_canvas, image=self.render_adj_matrix)
        self.img_adj_matrix.image = self.render_adj_matrix
        self.img_adj_matrix.place(x=0, y=0)

        return self.render_graph, self.render_adj_matrix

    def step_five(self):

        global left_height
        left_height = self.left.winfo_height()

        global left_width
        left_width = self.left.winfo_width()

        global right_height
        right_height = self.adj_matrix_canvas.winfo_height()

        global right_width
        right_width = self.adj_matrix_canvas.winfo_width()

        # Loading all the graph images
        load_graph_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/Graphv5.0.gif")
        # Get frame size
        load_graph_image = load_graph_image.resize((left_width, left_height))

        # Loading adjacency matrix images
        load_adj_mat_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/AdjacencyMatrixv5.0.gif")
        # Get frame size
        load_adj_mat_image = load_adj_mat_image.resize((right_width, right_height))

        # Render graph Images
        self.render_graph = ImageTk.PhotoImage(load_graph_image)
        # Displaying the graph image
        self.img_graph = tk.Label(self.left, image=self.render_graph)
        self.img_graph.image = self.render_graph
        self.img_graph.place(x=0, y=0)

        # Render Adjacency matrix images
        self.render_adj_matrix = ImageTk.PhotoImage(load_adj_mat_image)
        # Displaying the adjacency matrix images
        self.img_adj_matrix = tk.Label(self.adj_matrix_canvas, image=self.render_adj_matrix)
        self.img_adj_matrix.image = self.render_adj_matrix
        self.img_adj_matrix.place(x=0, y=0)

        return self.render_graph, self.render_adj_matrix

    def step_six(self):

        global left_height
        left_height = self.left.winfo_height()

        global left_width
        left_width = self.left.winfo_width()

        global right_height
        right_height = self.adj_matrix_canvas.winfo_height()

        global right_width
        right_width = self.adj_matrix_canvas.winfo_width()

        # Loading all the graph images
        load_graph_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/Graphv6.0.gif")
        # Get frame size
        load_graph_image = load_graph_image.resize((left_width, left_height))

        # Loading adjacency matrix images
        load_adj_mat_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/AdjacencyMatrixv6.0.gif")
        # Get frame size
        load_adj_mat_image = load_adj_mat_image.resize((right_width, right_height))

        # Render graph Images
        self.render_graph = ImageTk.PhotoImage(load_graph_image)
        # Displaying the graph image
        self.img_graph = tk.Label(self.left, image=self.render_graph)
        self.img_graph.image = self.render_graph
        self.img_graph.place(x=0, y=0)

        # Render Adjacency matrix images
        self.render_adj_matrix = ImageTk.PhotoImage(load_adj_mat_image)
        # Displaying the adjacency matrix images
        self.img_adj_matrix = tk.Label(self.adj_matrix_canvas, image=self.render_adj_matrix)
        self.img_adj_matrix.image = self.render_adj_matrix
        self.img_adj_matrix.place(x=0, y=0)

        return self.render_graph, self.render_adj_matrix

    def step_seven(self):

        global left_height
        left_height = self.left.winfo_height()

        global left_width
        left_width = self.left.winfo_width()

        global right_height
        right_height = self.adj_matrix_canvas.winfo_height()

        global right_width
        right_width = self.adj_matrix_canvas.winfo_width()

        # Loading all the graph images
        load_graph_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/Graphv7.0.gif")
        # Get frame size
        load_graph_image = load_graph_image.resize((left_width, left_height))

        # Loading adjacency matrix images
        load_adj_mat_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/AdjacencyMatrixv7.0.gif")
        # Get frame size
        load_adj_mat_image = load_adj_mat_image.resize((right_width, right_height))

        # Render graph Images
        self.render_graph = ImageTk.PhotoImage(load_graph_image)
        # Displaying the graph image
        self.img_graph = tk.Label(self.left, image=self.render_graph)
        self.img_graph.image = self.render_graph
        self.img_graph.place(x=0, y=0)

        # Render Adjacency matrix images
        self.render_adj_matrix = ImageTk.PhotoImage(load_adj_mat_image)
        # Displaying the adjacency matrix images
        self.img_adj_matrix = tk.Label(self.adj_matrix_canvas, image=self.render_adj_matrix)
        self.img_adj_matrix.image = self.render_adj_matrix
        self.img_adj_matrix.place(x=0, y=0)

        return self.render_graph, self.render_adj_matrix

    def step_eight(self):

        global left_height
        left_height = self.left.winfo_height()

        global left_width
        left_width = self.left.winfo_width()

        global right_height
        right_height = self.adj_matrix_canvas.winfo_height()

        global right_width
        right_width = self.adj_matrix_canvas.winfo_width()

        # Loading all the graph images
        load_graph_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/Graphv8.0.gif")
        # Get frame size
        load_graph_image = load_graph_image.resize((left_width, left_height))

        # Loading adjacency matrix images
        load_adj_mat_image = Image.open("C:/Users/AG/PycharmProjects/FYP/Assets/AdjacencyMatrixv8.0.gif")
        # Get frame size
        load_adj_mat_image = load_adj_mat_image.resize((right_width, right_height))

        # Render graph Images
        self.render_graph = ImageTk.PhotoImage(load_graph_image)
        # Displaying the graph image
        self.img_graph = tk.Label(self.left, image=self.render_graph)
        self.img_graph.image = self.render_graph
        self.img_graph.place(x=0, y=0)

        # Render Adjacency matrix images
        self.render_adj_matrix = ImageTk.PhotoImage(load_adj_mat_image)
        # Displaying the adjacency matrix images
        self.img_adj_matrix = tk.Label(self.adj_matrix_canvas, image=self.render_adj_matrix)
        self.img_adj_matrix.image = self.render_adj_matrix
        self.img_adj_matrix.place(x=0, y=0)

        return self.render_graph, self.render_adj_matrix

    def delete_image(self):

        self.render_graph = ImageTk.PhotoImage(image="LA", size=None)
        self.img_graph.image = self.render_graph

        self.render_adj_matrix = ImageTk.PhotoImage(image="LA", size=None)
        self.img_adj_matrix.image = self.render_adj_matrix


# Setting some window properties
root.title("Graph")
# Setting the window size based on the screen size
root.pack_propagate(0)
root.state('zoomed')
# # Making the window ful-screen
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# # print(screen_width, " ", screen_height)
# root.geometry("{0}x{1}+0+0".format(screen_width, screen_height))
root.focus_set()
root.update()
# Press the Esc key ends the program
root.bind('<Escape>', lambda e: e.widget.quit())
my_Window = Window(root)
root.mainloop()
