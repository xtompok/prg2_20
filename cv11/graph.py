import networkx as nx
# Matplotlib import is needed for graph visualisation
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()
# Add node
G.add_node(3)
# Add attribute for the node
G.nodes[3]['name']='tři'
# Also can be written as 
# G.add_node(3,name='tři')
G.add_edge(1,3)
G.edges[(3,1)]['name'] = '1--3'
G.add_edge(1,2)
G.add_edge(2,3)
# Batch add nodes
G.add_nodes_from([1,2,3,(4,{'name':'čtyři'}),5])
# Batch add edges
G.add_edges_from([(1,4),(1,5),(4,5)])
# Show the graph summary
print(nx.info(G))
# Show attributes of the graph node with name 1
print(G.nodes[1])
# Show attributes of the graph edge between nodes 1 and 3
print(G.edges[(1,3)])
# Show graph nodes (and their attributes)
print(G.nodes)

# Create labels for nodes in graph visualisation
# Key is the node name, value is the label to be shown for given node
labels = {}
for n in G.nodes:
    # Use 'name' attribute if present
    if 'name' in G.nodes[n]:
        labels[n] = G.nodes[n]['name']
    # Use node name otherwise
    else:
        labels[n] = n

# Draw graph with previously created labels
nx.draw(G, labels = labels, with_labels = True)
# Open the window with the graph. If omitted, nothing will be shown and program ends successfully.
plt.show()