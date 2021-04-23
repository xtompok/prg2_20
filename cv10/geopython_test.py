# Source: https://networkx.org/documentation/latest/auto_examples/geospatial/plot_lines.html

import geopandas
import matplotlib.pyplot as plt
import momepy
import networkx as nx
import contextily as cx

# %%
# Read in example street geometry from GeoJSON. Source of example data: OSM
streets = geopandas.read_file("streets.geojson")

f, ax = plt.subplots(figsize=(10, 10))
streets.plot(ax=ax)
ax.set_axis_off()
# %%
# Construct the primal graph. momepy automatically preserves all attributes
# from GeoDataFrame and stores then as edge attributes.
G = momepy.gdf_to_nx(streets, approach="primal")

# Plot
f, ax = plt.subplots(1, 2, figsize=(12, 6), sharex=True, sharey=True)
streets.plot(color="k", ax=ax[0])
for i, facet in enumerate(ax):
    facet.set_title(("Streets", "Graph")[i])
    facet.axis("off")
    cx.add_basemap(facet, crs=streets.crs.to_string())
nx.draw(G, {n: [n[0], n[1]] for n in list(G.nodes)}, ax=ax[1], node_size=50)

plt.show()