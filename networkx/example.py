import networkx as nx
import matplotlib.pyplot as plt     
G = nx.DiGraph() # directional graph 
G.add_node(1)              
G.add_nodes_from([2,3])
G.add_edge(1,2)                    
G.add_edges_from([(1,3),(2,3)])
nx.draw(G, with_labels=True)
plt.savefig("nw.png")
