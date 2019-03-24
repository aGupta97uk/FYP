import networkx as nx
import matplotlib.pyplot as plt
from tkinter import messagebox
from Interface import *
import matplotlib
matplotlib.use("TkAgg")


def get_graph(self):

    string_vertices = self.vertices_num.get()
    string_edges = self.edges_num.get()
    output_string = ''

    output_string += "Random Graph Generate: " + string_edges \
                     + " edge(s) and " + string_vertices + " vertice(s)\n"

    try:
        num_vertices = int(string_vertices)
        # print("Vertices number value is: ", num_vertices)

        num_edges = int(string_edges)
        # print("Edges number value is: ", num_edges)

        # Only accepted case where the graph is plotted.
        if (1 < num_vertices < 9) and (0 < num_edges < 65):
            # print("DRAW THE GRAPH NOW")
            self.redirect(output_string)
            draw_graph(self, num_vertices, num_edges)
        # Vertices Input Error
        elif num_vertices == 0:
            # print("Number of vertices entered: ", num_vertices)
            messagebox.showerror("Vertex Input Error", "There must be at least 2 vertices in the graph.")
            self.redirect("Vertex Input Error: There must be at least 2 vertices in the graph.\n")
        elif num_vertices == 1:
            # print("Number of vertices entered: ", num_vertices)
            messagebox.showerror("Vertex Input Error", "There must be at least 2 vertices in the graph.")
            self.redirect("Vertex Input Error: There must be at least 2 vertices in the graph.\n")
        elif num_vertices < 0:
            # print("Number of vertices entered: ", num_vertices)
            messagebox.showerror("Vertex Input Error",
                                 "The graph cannot contain a negative number of vertices.")
            self.redirect("Vertex Input Error: The graph cannot contain a negative number of vertices.\n")
        elif num_vertices > 8:
            # print("Number of vertices entered: ", num_vertices)
            messagebox.showerror("Vertex Input Error", "The graph cannot more than 8 vertices.")
            self.redirect("Vertex Input Error: The graph cannot more than 8 vertices.\n")
        # Edges Input Errors
        elif num_edges == 0:
            # print("Number of edges entered: ", num_edges)
            messagebox.showerror("Edge Input Error", "The graph must have at least 1 edge.")
            self.redirect("Edge Input Error: The graph must have at least 1 edge.\n")
        elif num_edges < 0:
            # print("Number of edges entered: ", num_edges)
            messagebox.showerror("Edge Input Error", "The graph cannot contain a negative number of edges.")
            self.redirect("Edge Input Error: The graph cannot contain a negative number of edges.\n")
        elif num_edges > 64:
            # print("Number of edges entered: ", num_edges)
            messagebox.showerror("Edge Input Error", "The graph cannot more than 64 edges.")
            self.redirect("Edge Input Error: The graph cannot more than 64 edges.\n")
    except ValueError:
        # print("Entered value is not a number")
        messagebox.showerror("INPUT ERROR", "A number must be entered.")
        self.redirect("INPUT ERROR: A number must be entered.\n")


# Drawing graph in the top left frame
def draw_graph(self, vertices, edges):

    self.ax.clear()
    self.toolbar.update()

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
    # Tight Figure Layout
    plt.tight_layout()
    # Turn off the axis
    plt.axis('off')

    # Drawing the figure using the renderer
    self.canvas.draw()
    # Positioning the canvas using pack
    self.canvas.get_tk_widget().pack(side="left", fill="both", expand=True)
    # Print Out some Graph info
    global graph_info
    graph_info = nx.info(graph)


def graph_properties(self):

    self.redirect(graph_info)
    self.redirect("\n")
