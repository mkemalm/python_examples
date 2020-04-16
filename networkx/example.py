import networkx as nx
import matplotlib.pyplot as plt     
G = nx.DiGraph() # directional graph 
G2 = nx.DiGraph() # directional graph 
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,3)
G2.add_nodes_from([1,2,3,4])
G2.add_edges_from([(1,3),(2,3),(2,1),(2,4),(3,4)])
plt.subplot(121)
nx.draw(G, with_labels=True)
plt.subplot(122)
nx.draw(G2, with_labels=True)
plt.savefig("nw.png")
