import geopandas
import networkx as nx 

# Open geodata file. Geopandas supports many formats (https://geopandas.org/docs/user_guide/io.html)
gdf = geopandas.read_file("holesovice.geojson")
print(type(gdf))
print(gdf)

# Create graph from the linestrings. Each break point is a node.
G = nx.Graph()
# gdf.iterrows returns an iterator over the features (similar to range)
for idx,r in gdf.iterrows():
    # Get coordinates
    coords = r.geometry.coords
    
    #print(idx)
    #print(",".join(map(str,r.geometry.coords)))

    # Remember last point for creating edges
    mempoint = r.geometry.coords[0]
    # Add edges (starting from second point, first we have in mempoint)
    for point in r.geometry.coords[1:]:
        # Point is a tuple containing coordinates -> it can be used as node name
        G.add_edge(mempoint,point)
        # Add the index of the feature as edge attribute
        G.edges[mempoint,point]['index'] = idx
        # Update the last point
        mempoint = point

print(nx.info(G))

# Get some node
v = list(G.nodes)[0]
# Run BFS in the graph G from the node v
print(list(nx.bfs_edges(G,v)))

# Možnosti výroby grafu z geodat ve formě linestringů:
#  a) vrcholy jsou koncové body linestringů
#     + reprezentace bude úspornější
#     - méně podrobné
#     - nemáme tak dobré informace o křížení
#     - rozbije se topologie, pokud nějaký linestring končí uprostřed jiného 
#  b) vrcholy jsou všechny body linestringů
#     + bude to přesněji reprezentovat skutečnost
#     - graf bude větší co do počtu hran a vrcholů
