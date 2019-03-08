import networkx as nx
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
                                         padx=5, pady=5, background='white')
        self.left_frame.pack(side="left", fill="both", expand=True)

        # Right Frame
        self.right_frame = tk.Frame(self.main_container, background='blue')
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Right Frame2 - Top
        self.right_frame2_top = tk.Frame(self.right_frame, relief="ridge", bd=20, borderwidth=3,
                                         padx=5, pady=5, background='green')
        self.right_frame2_top.grid(row=0, column=1, sticky="nsew")
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(1, weight=1)

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
                                    command=lambda: self.get_graph())
        self.button_grg.grid(row=3, column=1)
        self.button_grg.grid_rowconfigure(1, weight=1)

        # Creating the Figure
        fig_num = 1
        self.figure = plt.figure(num=fig_num, dpi=100, clear=True)
        self.ax = self.figure.add_subplot(111)

        # Defining the canvas
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.left_frame)

    #
    #     # Right Frame2 - Middle
    #     self.right_frame2_mid = tk.Frame(self.right_frame2, relief="ridge", bd=20, borderwidth=3,
    #                                      padx=5, pady=5)
    #     self.right_frame2_mid.grid(row=4, column=0, sticky="nsew")
    #     self.right_frame2.grid_rowconfigure(4, weight=1)
    #     self.right_frame2.grid_columnconfigure(0, weight=1)
    #
    #     # Label - Algorithms
    #     self.lab_alg = tk.Label(self.right_frame2_mid, text="Algorithms",
    #                             font="24")
    #     self.lab_alg.grid(row=0, column=0, padx=10, pady=10, in_=self.right_frame2_mid)
    #
    #     # Right Frame2 - Bottom
    #     self.right_frame2_bottom = tk.Frame(self.right_frame2, relief="ridge", bd=20, borderwidth=3,
    #                                      padx=5, pady=5)
    #     self.right_frame2_bottom.grid(row=8, column=0, sticky="nsew")
    #     self.right_frame2.grid_rowconfigure(4, weight=1)
    #     self.right_frame2.grid_columnconfigure(0, weight=1)
    #
    #     # # Text area to print out the results of the algorithm run
    #     # # FIXME: This makes the top and bottom frames resize, making the top frame smaller
    #     # # This happens only when Text is used. Label is fine
    #     # self.right_frame2_bottom_text = tk.Text(self.right_frame2_bottom, background="Light Grey", relief="ridge",
    #     #                                        bd=20, borderwidth=3, pady=2, padx=2)
    #     # self.right_frame2_bottom_text.grid(side="bottom", fill='both', expand=True, anchor="center")
    #
    # Getting the number of vertices for the random graph
    # Performs validation checks on the user input to make sure the input entered is correct
    # TODO: Add a upper limit to the input validation
    # FIXME: A new graph is drawn every time underneath the old one

    def get_graph(self):

        string_vertices = self.vertices_num.get()
        string_edges = self.edges_num.get()

        try:
            num_vertices = int(string_vertices)
            print("Vertices number value is: ", num_vertices)

            num_edges = int(string_edges)
            print("Edges number value is: ", num_edges)

            # Only accepted case where the graph is plotted.
            if (1 < num_vertices < 9) and (0 < num_edges < 65):
                print("DRAW THE GRAPH NOW")
                self.draw_graph(num_vertices, num_edges)
            # Vertices Input Error
            elif num_vertices == 0:
                print("Number of vertices entered: ", num_vertices)
                messagebox.showerror("Vertex Input Error", "There must be at least 2 vertices in the graph.")
            elif num_vertices == 1:
                print("Number of vertices entered: ", num_vertices)
                messagebox.showerror("Vertex Input Error", "There must be at least 2 vertices in the graph.")
            elif num_vertices < 0:
                print("Number of vertices entered: ", num_vertices)
                messagebox.showerror("Vertex Input Error", "The graph cannot contain a negative number of vertices.")
            elif num_vertices > 8:
                print("Number of vertices entered: ", num_vertices)
                messagebox.showerror("Vertex Input Error", "The graph cannot more than 8 vertices.")
            # Edges Input Errors
            elif num_edges == 0:
                print("Number of edges entered: ", num_edges)
                messagebox.showerror("Edge Input Error", "The graph must have at least 1 edge.")
            elif num_edges < 0:
                print("Number of edges entered: ", num_edges)
                messagebox.showerror("Edge Input Error", "The graph cannot contain a negative number of edges.")
            elif num_edges > 64:
                print("Number of edges entered: ", num_edges)
                messagebox.showerror("Edge Input Error", "The graph cannot more than 64 edges.")
        except ValueError:
            print("Entered value is not a number")
            messagebox.showerror("INPUT ERROR", "A number must be entered.")

    # Drawing graph in the top left frame
    def draw_graph(self, vertices, edges):

        self.ax.clear()

        # TODO: Change the type of graph so only a complete graph is generated
        # NetworkX Graph
        graph = nx.dense_gnm_random_graph(vertices, edges)
        pos = nx.spring_layout(graph)
        # Draw Nodes
        nx.draw_networkx_nodes(graph, pos, ax=self.ax, node_size=700)
        # Draw Edges
        nx.draw_networkx_edges(graph, pos, width=2)
        # Draw labels
        nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif')
        # Turn off the axis
        plt.axis('off')

        # Drawing the figure using the renderer
        self.canvas.draw()
        # Positioning the canvas using pack
        self.canvas.get_tk_widget().pack(side="left", anchor="center", fill="both", expand=True)

        print("Number of edges in graph: ", nx.info(graph))

        num_vertices = nx.number_of_nodes(graph)
        num_edges = nx.number_of_edges(graph)

        print("Number of Vertices = ", num_vertices)
        print("Number of Edges = ", num_edges)


# Setting some window properties
root.title("Graph")
# Setting the window size based on the screen size
root.pack_propagate(0)
# Making the window ful-screen
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
