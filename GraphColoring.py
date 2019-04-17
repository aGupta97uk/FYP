# Vertex Coloring - Greedy Coloring Heuristic
# Greedy coloring to find optimal colorings in polynomial time.
# Implementing the welsh_powell algorithm

import matplotlib.pyplot as plt
import networkx as nx
from Interface import *
from tkinter import messagebox


def get_gc(self):
    graph = my_graph()
    col_list = welsh_powell(graph)
    draw_graph(self, graph, col_list)


# Read the input from the file and draw a graph.
def my_graph():
    # Empty NetworkX graph
    graph = nx.Graph()
    # Open the file for reading
    file = open("Random Graph.txt", "r")
    # Read info from the file line by line.
    # This is needed because there can be 2-5 characters (including one space).
    # Simply reading a certain number of character's won't work.
    info = int(file.readline())
    for edge in range(info):
        graph_edge_list = file.readline().split()
        graph.add_edge(graph_edge_list[0], graph_edge_list[1])
    # Close file
    file.close()

    return graph


def welsh_powell(graph):
    # Sorting the nodes in descending order of degree
    node_list = sorted(list(graph.nodes()), key=lambda x: len(graph[x]), reverse=True)
    col_list = {}
    # Assign the first colour to the first node
    col_list[node_list[0]] = 0
    # Assigning colors to the remaining nodes
    for node in node_list[1:]:
        available = [True] * len(graph.nodes())

        # Iterating through all the adjacent nodes and mark the color unavailable if the color has already been used
        for adj_node in graph.neighbors(node):
            if adj_node in col_list.keys():
                col = col_list[adj_node]
                available[col] = False

        clr = 0
        for clr in range(len(available)):
            if available[clr] == True:
                break
        col_list[node] = clr

    return col_list


# Drawing the colored graph. Replacing the old one
def draw_graph(self, graph, col_list):

    self.ax.clear()
    self.toolbar.update()

    # TODO: Change the type of graph so only a complete graph is generated
    # NetworkX Graph
    pos = nx.spring_layout(graph)
    # List of colors to color nodes
    values = [col_list.get(node, "yellow") for node in graph.nodes()]
    # Draw Graph
    nx.draw(graph, pos, ax=self.ax, node_size=700, node_color=values)
    # Draw labels
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif')
    # Tight Figure Layout
    plt.tight_layout()
    # Turn off the axis
    plt.axis('off')

    # Drawing the figure using the renderer
    self.canvas.draw()
    # Positioning the canvas using pack
    self.canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

    global val
    val = len(set(values))

    num_colors(self)

    return val


def colors_used(self):

    self.redirect("Num colors used to color all Vertices: ")
    self.redirect(val)
    self.redirect("\n")


# Print out the number of distinct colours used to color the graph
def num_colors(self):

    self.redirect("The algorithm was successfully run.")
    self.redirect("\n")


def check_num_colors_answer(self):

    user_input = self.entry_num_colors.get()

    try:
        input_answer = int(user_input)

        if input_answer == val:
            self.redirect("Correct Answer!\n")
        elif input_answer < 0:
            self.redirect("The number of colors cannot be less than 0.\n")
        elif input_answer == 0:
            self.redirect("The number of colors cannot be equal to 0.\n")
        elif input_answer == 1:
            self.redirect("The minimum number of colours required will always be 2.\n")
        elif 1 < input_answer:
            self.redirect("Incorrect Answer!\n")
    except ValueError:
        messagebox.showerror("INPUT ERROR", "A number must be entered.")
        self.redirect("INPUT ERROR: A number must be entered.\n")

