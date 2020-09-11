import networkx as nx
import matplotlib.pyplot as plt
import os

gr = nx.read_edgelist('networks.txt')

print(gr.nodes)

drawPos = nx.random_layout(gr)

# nx.draw_networkx(gr,drawPos)

print(nx.node_link_data(gr))
nx.write_gexf(gr,'selam.gexf')

grGexf = nx.read_gexf('selam.gexf')

agr = nx.read_edgelist('AgirlikliNetwork.txt', data =[("weight", float),("color",str)])

colors = [d["color"] for s, t, d in agr.edges(data =True)]       
nx.draw_networkx(agr, width=4, edge_color=colors)
plt.gca().margins(0.15, 0.15)
plt.show()
