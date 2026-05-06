import networkx as nx
import matplotlib.pyplot as plt

# Your graph
graph = {
#add your (code) graph here as a dictionary
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []

}

# Create directed graph
G = nx.DiGraph()

# Add edges
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Add isolated nodes (leaf nodes with no outgoing edges)
for node in graph:
    if node not in G:
        G.add_node(node)

# Draw
plt.figure(figsize=(6, 5))
pos = nx.spring_layout(G)  # auto layout

nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True
)

plt.title("Graph Representation")
plt.show()

print("BFS:", bfs(graph, 'A')) #add function calls with their respective arguments
print("DFS:", dfs(graph, 'A')) #add function calls with their respective arguments
print("IDDFS:", iddfs(graph, 'A', 3)) #add function calls with their respective arguments