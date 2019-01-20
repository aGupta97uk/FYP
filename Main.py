import networkx as nx
import matplotlib.pyplot as plt

from Interface import Window

G = nx.Graph()

# Vertex
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')

# Edge
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=2)
G.add_edge('A', 'D', weight=3)
G.add_edge('A', 'E', weight=4)
G.add_edge('A', 'F', weight=5)
G.add_edge('B', 'C', weight=6)

# Using the shortest path algorithm
print(nx.shortest_path(G, 'C', 'B', weight='weight'))

# Some Information about the graph
print(nx.info(G))

print("Number of edges:", nx.number_of_edges(G))

print(G.node)

# draw graph
nx.draw_networkx(G, pos=nx.spring_layout(G, weight='weight'))
# turn off the axis on the graph
plt.axis('off')
# display the drawn graph
plt.show()

Window()
